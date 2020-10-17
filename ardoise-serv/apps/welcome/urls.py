from django.urls import path, include
from .views.logged import LoggedView
from .views.index import IndexView

urlpatterns = [
    path('', IndexView.as_view()),
    path('logged/', LoggedView.as_view())
]
