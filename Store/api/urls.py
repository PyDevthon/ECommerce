from django.urls import path
from . import views


urlpatterns = [
    path('Contact', views.ContactCreteView.as_view(), name='api_create_contact'),
]

