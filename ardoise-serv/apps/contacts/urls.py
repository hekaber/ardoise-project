from django.urls import path, include
from .views.contact_details import ContactList


urlpatterns = [
    path('', ContactList.as_view()),
]
