from flask_fixture import endpoint
import pytest

@pytest.fixture
@endpoint('/')
def root():
    return 'kek'
