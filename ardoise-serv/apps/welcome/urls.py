from django.urls import path, include
from .views import LoggedView

urlpatterns = [
    path('logged/', LoggedView.as_view())
]
