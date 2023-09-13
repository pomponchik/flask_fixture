import urllib

import requests
import pytest

import urllib.parse
>>> urllib.parse.urljoin(url1, url2)


@pytest.mark.timeout(30)
def test_run_server(local_server_url):
    assert requests.get(local_server_url).text == 'kek'


@pytest.mark.timeout(30)
def test_render_simple_template(local_server_url):
    page_url = urllib.parse.urljoin(local_server_url, 'simple_template')
    assert requests.get(page_url).text
