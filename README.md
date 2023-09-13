![logo](https://raw.githubusercontent.com/pomponchik/flask_fixture/main/docs/assets/logo_5.png)

[![Downloads](https://static.pepy.tech/badge/flask_fixture/month)](https://pepy.tech/project/flask_fixture)
[![Downloads](https://static.pepy.tech/badge/flask_fixture)](https://pepy.tech/project/flask_fixture)
[![codecov](https://codecov.io/gh/pomponchik/flask_fixture/graph/badge.svg?token=8iyMsUaLvN)](https://codecov.io/gh/pomponchik/flask_fixture)
[![Test-Package](https://github.com/pomponchik/flask_fixture/actions/workflows/tests_and_coverage.yml/badge.svg)](https://github.com/pomponchik/flask_fixture/actions/workflows/tests_and_coverage.yml)
[![Python versions](https://img.shields.io/pypi/pyversions/flask_fixture.svg)](https://pypi.python.org/pypi/flask_fixture)
[![PyPI version](https://badge.fury.io/py/flask_fixture.svg)](https://badge.fury.io/py/flask_fixture)


A simple plugin for [Pytest](https://docs.pytest.org/) containing a [fixture](https://docs.pytest.org/explanation/fixtures.html) that can start and stop the [Flask server](https://flask.palletsprojects.com/server/) to run related tests. You just have to define the [routes](https://flask.palletsprojects.com/quickstart/#routing).

Install it by the command:

```bash
pip install flask_fixture
```

Define some routes in your `conftest.py` file:

```python
from flask_fixture import endpoint

@endpoint('/')
def root():
    return 'some text'
```

And use a URL of a server in your tests as a fixture `local_server_url`:

```python
import requests

def test_server(local_server_url):
    assert requests.get(local_server_url).text == 'some text'
```

The example uses the [Requests](https://requests.readthedocs.io/en/latest/) library.
