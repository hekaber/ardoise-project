from django.urls import path, include
from .views.contact_list import ContactFriendsListView, ContactListView


urlpatterns = [
    path('friends/', ContactFriendsListView.as_view(), name="ContactFriendsListView"),
    path('list/', ContactListView.as_view(), name="ContactListView"),
]
