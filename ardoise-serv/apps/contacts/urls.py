from django.urls import path, include
from .views.contact_list import ContactListView
from .views.invite import InviteView


urlpatterns = [
    path('list/', ContactListView.as_view(), name="ContactListView"),
    path('invite/', InviteView.as_view(), name="InviteView"),
]
