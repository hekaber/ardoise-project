from django.urls import path, include
from .views.contact_list import ContactListView


urlpatterns = [
    path('list/', ContactListView.as_view(), name="ContactListTemplateView"),
]
