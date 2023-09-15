import os
import io
import logging
import traceback
from typing import Dict, List, Any
from contextlib import redirect_stdout, redirect_stderr
from multiprocessing import Queue

from flask import Flask
from awaits import shoot

from flask_fixture.state_storage.collection_of_routes import routes
from flask_fixture.dataclasses.running_startup_result import RunningStartupResult
from flask_fixture.dataclasses.output_chunk import ChunkType, ProcessOutputChunk


class QueueHandler(logging.Handler):
    def __init__(self, queue: Queue):
        logging.Handler.__init__(self)
        self.queue = queue

    def emit(self, record: logging.LogRecord):
        chunk: ProcessOutputChunk = ProcessOutputChunk(value=record, type=ChunkType.LOG_RECORD)
        self.queue.put(chunk)

@shoot
def emit_output(queue, buffer, chunk_type):
    while True:
        string = buffer.getvalue()
        chunk: ProcessOutputChunk = ProcessOutputChunk(value=string, type=chunk_type)
        self.queue.put(chunk)

def run_flask(queue: Queue, port: int, modules: List[str], configs: Dict[str, Any]) -> None:
    """
    The function is designed to run in a separate process. It starts the flask server.

    Before starting the server, it does some manipulations:
    1. Imports all modules that used the @endpoint decorator. This is necessary so that the decorator code is executed in the child process, and the list of endpoints descriptions is filled in.
    2. The Flask application is created and all the endpoints collected in the first step are registered in it.

    The server output (both stderr and stdout) is redirected to the trash.

    The queue is used to synchronize with the process that started this function. After the function is started, that process starts waiting for the function to put something in the queue. Thus, it is guaranteed that the starting process will not continue its execution before the server initialization occurs. This approach allows you to do without using sleep().
    """
    startup_result = RunningStartupResult(success=True, routes=[])
    try:
        for module in modules:
            __import__(module)

        app = Flask('flask_fixture', os.path.abspath(configs['template_folder']))

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

    buffer_stdout = io.StringIO()
    buffer_stderr = io.StringIO()
    emit_output(queue, buffer_stdout, ChunkType.STDOUT)
    emit_output(queue, buffer_stderr, ChunkType.STDERR)

    with redirect_stdout(buffer_stdout), redirect_stderr(buffer_stderr):
        app.run(port=port)
