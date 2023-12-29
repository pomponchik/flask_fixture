import os
import io
import logging
import traceback
from typing import Dict, List, Type, Callable, Union, Any
from contextlib import redirect_stdout, redirect_stderr
from multiprocessing import Queue

from flask import Flask

from flask_fixture.state_storage.collection_of_routes import routes
from flask_fixture.dataclasses.running_startup_result import RunningStartupResult
from flask_fixture.logging.queue_handler import QueueHandler


def run_flask(queue: Queue, port: int, modules: List[str], configs: Dict[str, Any], flask_app_fabric: Union[Type, Callable] = Flask) -> None:
    """
    The function is designed to run in a separate process. It starts the flask server.

    Before starting the server, it does some manipulations:
    1. Imports all modules that used the @endpoint decorator. This is necessary so that the decorator code is executed in the child process, and the list of endpoints descriptions is filled in.
    2. The Flask application is created and all the endpoints collected in the first step are registered in it.

    The server output (both stderr and stdout) is redirected to the trash.

    The queue is used to synchronize with the process that started this function. After the function is started, that process starts waiting for the function to put something in the queue. Thus, it is guaranteed that the starting process will not continue its execution before the server initialization occurs. This approach allows you to do without using sleep().
    """
    startup_result = RunningStartupResult(success=True, routes=[], configs=configs)
    try:
        for module in modules:
            __import__(module)

        app = flask_app_fabric('flask_fixture', template_folder=os.path.abspath(configs['template_folder']))

        for route in routes:
            startup_result.routes.append(str(route))
            routing = app.route(*(route.args), **(route.kwargs))
            routing(route.function)

        handler = QueueHandler(queue)
        logging.root.addHandler(handler)

    except Exception as e:
        startup_result.success = False

        buffer = io.StringIO()
        traceback.print_exception(e, file=buffer)
        traceback_string = buffer.getvalue()

        startup_result.traceback = traceback_string
        startup_result.exception_name = e.__class__.__name__
        startup_result.exception_string = str(e)

    finally:
        queue.put(startup_result)
        if not startup_result.success:
            return

    with open(os.devnull, 'w') as devnull:
        with redirect_stdout(devnull), redirect_stderr(devnull):
            app.run(port=configs['port'])
