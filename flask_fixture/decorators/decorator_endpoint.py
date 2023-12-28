import inspect
from typing import Any, Callable

from flask_fixture.dataclasses.route_item import RouteItem
from flask_fixture.state_storage.collection_of_routes import routes
from flask_fixture.state_storage.collection_of_importing_modules import modules
from flask_fixture.errors import NeedToDefineURLError


def endpoint(*args: Any, **kwargs: Any) -> Callable[[Callable[[Any], Any]], Callable[[Any], Any]]:
    """
    A decorator factory that registers endpoints in the Flask application.

    The URL (in short form) should always be passed here as the first positional argument.
    If it is not passed, the NeedToDefineURLError exception will be raised.

    All arguments that will be passed to this function will be used in the same form when creating routes for the Flask server.
    """
    if not args:
        raise NeedToDefineURLError('The first argument to the decorator is to pass the expected URL.')
    elif len(args) == 1 and callable(args[0]) and not kwargs:
        raise NeedToDefineURLError('The first argument to the decorator is to pass the expected URL.')

    def decorator(function: Callable[[Any], Any]) -> Callable[[Any], Any]:
        """
        This decorator simply adds the signatures of the registered routes to a global list.
        This list will be recreated in the generated process, and the data from it will be used to create Flask routes.
        """
        routes.append(
            RouteItem(
                args=args,
                kwargs=kwargs,
                function=function,
            )
        )
        modules.add(inspect.getmodule(function).__name__)
        return function
    return decorator
