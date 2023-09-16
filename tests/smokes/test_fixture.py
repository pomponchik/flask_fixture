import os
import urllib
import time

import requests
import pytest

import urllib.parse


@pytest.mark.timeout(30)
def test_run_server(local_server_url):
    assert requests.get(local_server_url).text == 'kek'


@pytest.mark.timeout(30)
def test_render_simple_template(local_server_url):
    page_url = urllib.parse.urljoin(local_server_url, 'simple_template')
    page = requests.get(page_url).text

    with open(
        os.path.join(
            'tests',
            'smokes',
            'data',
            'templates',
            'index.html',
        ),
        'r',
    ) as file:
        file_content = file.read()
        assert file_content.strip() == page.strip()
