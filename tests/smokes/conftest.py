import pytest
from flask_fixture import endpoint


@pytest.fixture
@endpoint('/')
def root():
    return 'kek'
