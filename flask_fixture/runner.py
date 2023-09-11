from bottle import route, run, template

from flask_fixture.collection_of_routes import routes


def run_flask(queue, port, app_fabric):
    """
    Функция запускает сервер Flask для выполнения тестов.
    """
    for route in routes:
        print('add route', route)
        routing = route(*(route.args), **(route.kwargs))
        routing(route.function)

    queue.put(None)

    run(host='localhost', port=port)
