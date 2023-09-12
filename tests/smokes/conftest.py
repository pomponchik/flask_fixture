from flask_fixture import endpoint
import pytest


@endpoint('/')
def root():
    return 'kek'
