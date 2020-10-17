from django.urls import path, include
from .views.ticket_list import TicketListTemplateView
from .views.add_ticket import TicketCreateView


urlpatterns = [
    path('list/', TicketListTemplateView.as_view(), name="TicketListTemplateView"),
    path('add/', TicketCreateView.as_view(), name="TicketCreateView"),
]
