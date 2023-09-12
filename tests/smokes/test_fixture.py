import os

import pytest
import requests


@pytest.mark.timeout(60)
def test_run_server(local_server_url, root):
    from time import sleep

    print('url:', local_server_url)
    print(requests.get(local_server_url).text)
    print('THIS PID:', os.getpid())
    assert requests.get(local_server_url).text == 'kek'
