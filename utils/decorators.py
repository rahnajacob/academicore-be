from rest_framework.exceptions import NotFound
from courses.models import Course
from rest_framework.response import Response

def handle_exceptions(handler_func):
    def wrapper(*args, **kwargs):
        try:
            return handler_func(*args, **kwargs)
        except (Course.DoesNotExist, NotFound) as e:
            print(type(e))
            return Response({'message: course not found'}, 404)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
            return Response("unknown error occured", 500)
    return wrapper