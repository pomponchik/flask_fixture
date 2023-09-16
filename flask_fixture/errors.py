class NeedToDefineURLError(Exception):
    """
    This exception is raised if the user has not passed arguments to the decorator.
    """

class NotExpectedConfigFieldError(Exception):
    pass

class UnsuccessfulProcessStartupError(Exception):
    pass
