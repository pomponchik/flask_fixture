import os

import pytest
from flask import render_template

from flask_fixture import endpoint


@endpoint('/')
def root():
    return 'kek'


@endpoint('/simple_template')
def simple_template():
    return render_template(
        os.path.join(
            'tests',
            'smokes',
            'data',
            'templates',
            'index.html',
        )
    )
