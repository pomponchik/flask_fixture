from flask_fixture import endpoint


@endpoint('/')
def root():
    return 'kek'
