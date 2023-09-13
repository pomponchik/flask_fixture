import multiprocessing

import pytest

from flask_fixture.runner import run_flask
from flask_fixture.collection_of_routes import routes


@pytest.fixture(scope='session')
def local_server_url(local_server_port: int = 5001) -> str:
    """
    Run and shutdown the flask server, return a URL of the server.
    """
    modules = {x.module for x in routes}
    queue = multiprocessing.Queue()

    process = multiprocessing.Process(target=run_flask, args=(queue, local_server_port, modules))
    process.start()
    queue.get()

    yield f'http://localhost:{local_server_port}/'
    
    process.terminate()
