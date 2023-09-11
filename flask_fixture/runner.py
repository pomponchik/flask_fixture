from flask import render_template

from flask_fixture.collection_of_routes import routes


def run_flask(queue, port, app_fabric):
    """
    Функция запускает сервер Flask для выполнения тестов.
    """
    app = app_fabric('flask_fixture')

    for route in routes:
        print('add route', route)
        routing = app.route(*(route.args), **(route.kwargs))
        routing(route.function)

    queue.put(None)

    app.run(port=port)
