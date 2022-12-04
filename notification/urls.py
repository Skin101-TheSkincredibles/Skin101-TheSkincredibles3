from django.urls import path
from .views import set_notification, get_notification, show_notification

urlpatterns = [
    path('set-notification', set_notification, name='set-notification'),
    path('get-notification', get_notification, name='get-notification'),
    path('show-notification', show_notification, name='show-notification'),
]