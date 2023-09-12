import os
import importlib

from flask import Flask

from flask_fixture.collection_of_routes import routes


def run_flask(queue, port, files_with_routes, modules):
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

    app.run(port=port)
