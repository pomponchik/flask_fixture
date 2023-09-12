import importlib

from flask import Flask

from flask_fixture.collection_of_routes import routes


def run_flask(queue, port, files_with_routes):
    """
    Функция запускает сервер Flask для выполнения тестов.
    """


    for file_name in files_with_routes:
        spec = importlib.util.spec_from_file_location('kek', os.path.abspath(python_file))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

    app = Flask('flask_fixture')

    for route in routes:
        print('add route', route)
        routing = route(*(route.args), **(route.kwargs))
        routing(route.function)

    queue.put(None)

    app.run(port=port)
