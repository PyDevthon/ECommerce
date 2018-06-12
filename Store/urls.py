from django.urls import re_path, path
from . import views

urlpatterns = [
    re_path(r'^$', views.Home.as_view(), name='Home_Page'),
    path('Details/<int:key>', views.Details.as_view(), name='Item_Detail')
]
