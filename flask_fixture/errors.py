from flask_fixture.dataclasses.running_startup_result import RunningStartupResult

class NeedToDefineURLError(Exception):
    """
    This exception is raised if the user has not passed arguments to the decorator.
    """

class NotExpectedConfigFieldError(Exception):
    pass

class UnsuccessfulProcessStartupError(Exception):
    startup_result: RunningStartupResult
    traceback_string: str
