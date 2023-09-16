import os

import pytest
from flask import render_template

from flask_fixture import endpoint, config


@config
class MyConfig:
    template_folder: str = os.path.join(
        'tests',
        'smokes',
        'data',
        'templates',
    )

@endpoint('/')
def root():
    return 'kek'


@endpoint('/simple_template')
def simple_template():
    return render_template('index.html')
