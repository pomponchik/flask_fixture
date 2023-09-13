from typing import Any

from flask_fixture.route_item import RouteItem
from flask_fixture.collection_of_routes import routes
from flask_fixture.errors import NeedToDefineURLError


def endpoint(*args: Any, **kwargs: Any):
    if not args:
        raise NeedToDefineURLError('The first argument to the decorator is to pass the expected URL.')
    elif len(args) == 1 and callable(args[0]) and not kwargs:
        raise NeedToDefineURLError('The first argument to the decorator is to pass the expected URL.')

    def decorator(function):
        routes.append(
            RouteItem(
                args=args,
                kwargs=kwargs,
                function=function,
            )
        )
        return function
    return decorator
