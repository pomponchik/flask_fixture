import os
import importlib
from contextlib import redirect_stdout, redirect_stderr

from flask import Flask

from flask_fixture.collection_of_routes import routes
with contextlib.redirect_stdout()


def run_flask(queue, port, modules):
    """
    Функция запускает сервер Flask для выполнения тестов.
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
