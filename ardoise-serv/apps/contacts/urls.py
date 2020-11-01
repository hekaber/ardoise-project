
from django.urls import path
from .views.contact_list import ContactFriendsListView, ContactListView
from .views.invite import InviteView, InviteConfirmationView

urlpatterns = [
    path('friends/', ContactFriendsListView.as_view(), name="ContactFriendsListView"),
    path('', ContactListView.as_view(), name="ContactListView"),
    path('invite/', InviteView.as_view(), name="InviteView"),
    path('invite/confirmed/', InviteConfirmationView.as_view(), name="InviteConfirmationView"),
]
