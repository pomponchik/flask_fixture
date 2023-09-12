import importlib

from flask_fixture.collection_of_routes import routes


def run_flask(queue, port, app_fabric):
    """
    Функция запускает сервер Flask для выполнения тестов.
    """
    files_with_routes = {x.path for x in routes}

    for file_name in files_with_routes:
        spec = importlib.util.spec_from_file_location('kek', os.path.abspath(python_file))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

    for route in routes:
        print('add route', route)
        routing = route(*(route.args), **(route.kwargs))
        routing(route.function)

    queue.put(None)

    run(host='localhost', port=port)
