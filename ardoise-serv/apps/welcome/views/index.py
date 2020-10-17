from django.views.generic import TemplateView
import pathlib


class IndexView(TemplateView):

    template_name = 'welcome/index.html'

    def get(self, request, *args, **kwargs):
        current_path = pathlib.Path(__file__).parent.absolute()
        return super().get(request, *args, **kwargs)
