import requests


def test_run_server(local_server_url, root):
    assert requests.get(local_server_url).text == 'kek'
