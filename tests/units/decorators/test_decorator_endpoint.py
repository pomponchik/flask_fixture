import pytest

from flask_fixture import endpoint
from flask_fixture.errors import NeedToDefineURLError


def test_endpoint_without_arguments():
    with pytest.raises(NeedToDefineURLError):
        @endpoint()
        def kek():
            pass


def test_endpoint_without_breakets():
    with pytest.raises(NeedToDefineURLError):
        @endpoint
        def kek():
            pass
