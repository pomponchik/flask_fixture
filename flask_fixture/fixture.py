import multiprocessing

import pytest

from flask_fixture.runner import run_flask
from flask_fixture.state_storage.collection_of_importing_modules import modules
from flask_fixture.state_storage.collection_of_configs import configs
from flask_fixture.errors import NotExpectedConfigFieldError, UnsuccessfulProcessStartupError
from flask_fixture.logging.listener import listen_logs


@pytest.fixture(scope='session')
def local_server_url(local_server_port: int = 5001) -> str:
    """
    A fixture that starts and then stops the Flask server through a separate process.

    A queue is used to synchronize with the generated process.
    The current process makes sure that initialization in the generated process has ended by receiving a message from the queue.

    The names of modules that need to be imported so that all @endpoint decorators are executed are also passed to the generated process.

    The fixture returns the URL of the server, where you can immediately make requests, taking into account the registered routes.
    """
    for config_field_name, config_field_value in configs.items():
        if config_field_value is None:
            raise NotExpectedConfigFieldError()

    queue = multiprocessing.Queue()

    process = multiprocessing.Process(target=run_flask, args=(queue, local_server_port, list(modules), configs))

    process.start()
    startup_result = queue.get()
    if not startup_result.success:
        exception = UnsuccessfulProcessStartupError(f'Error {startup_result.exception_name}("{startup_result.exception_string}") when starting the process with the Flask server.')
        exception.startup_result = startup_result
        exception.traceback_string = startup_result.traceback
        raise exception

    listen_logs(queue)

    yield f'http://localhost:{configs["port"]}/'

    process.terminate()
