import requests
import pytest


@pytest.mark.timeout(180)
def test_run_server(local_server_url):
    assert requests.get(local_server_url).text == 'kek'
