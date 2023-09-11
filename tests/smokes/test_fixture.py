import requests

from flask_fixture import endpoint


@endpoint('/')
def root():
    return 'kek'


def test_run_server(local_server_url):
    assert requests.get(local_server_url).text == 'kek'
