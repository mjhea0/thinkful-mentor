import json
from functools import wraps

from flask import request, Response


def accept(mimetype):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if mimetype in request.accept_mimetypes:
                return func(*args, **kwargs)
            message = "Request must accept {} data".format(mimetype)
            data = json.dumps({"message": message})
            return Response(data, 406, mimetype="application/json")
        return wrapper
    return decorator


def require(mimetype):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if (request.mimetype == mimetype):
                return func(*args, **kwargs)
            message = "Request must contain {} data".format(mimetype)
            data = json.dumps({"message": message})
            return Response(data, 415, mimetype="application/json")
        return wrapper
    return decorator
