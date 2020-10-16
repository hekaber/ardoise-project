from django.conf import settings
from django.contrib.auth.backends import ModelBackend


class MiddlewareTest:
    def __init__(self, get_response):
        self.get_response = get_response
        self.translations = {
            "en": {"greeting": "Hello", "header": "Welcome Django!"},
            "fr": {"greeting": "Fuckerli", "header": "Fucker Django!"},
        }

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if settings.DEBUG:
            print('fuckerli')
            print(exception.__class__.__name__)
            print(exception)
        return None

    def process_template_response(self, request, response):
        if "fr" in request.META["HTTP_ACCEPT_LANGUAGE"]:
            response.context_data["translations"] = self.translations
            return response
        return response
