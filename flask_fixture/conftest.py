import multiprocessing
from typing import Callable

import pytest
from flask import Flask

from flask_fixture.runner import run_flask


@pytest.fixture(scope='session')
def local_server_url() -> str:
    """
    Run and shutdown the flask server, return a URL of the server.
    """

    port: int = 5001
    app_fabric: Callable = Flask

    queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=run_flask, args=(queue, port, app_fabric))
    process.start()
    queue.get()
    yield f'http://localhost:{port}/'
    process.terminate()
