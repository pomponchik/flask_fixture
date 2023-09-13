import os
from contextlib import redirect_stdout, redirect_stderr

from flask import Flask

from flask_fixture.collection_of_routes import routes


def run_flask(queue, port, modules):
    """
    The function is designed to run in a separate process. It starts the flask server.

    Before starting the server, she does some manipulations:
    1. Imports all modules that used the @endpoint decorator. This is necessary so that the decorator code is executed in the child process, and the list of endpoints descriptions is filled in.
    2. The Flask application is created and all the endpoints collected in the first step are registered in it.

    The server output (both stderr and stdout) is redirected to the trash.
    """
    for module in modules:
        __import__(module)

    app = Flask('flask_fixture')

    for route in routes:
        routing = app.route(*(route.args), **(route.kwargs))
        routing(route.function)

    queue.put(None)

    with open(os.devnull, 'w') as devnull:
        with redirect_stdout(devnull), redirect_stderr(devnull):
            app.run(port=port)
