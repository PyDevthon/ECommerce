from django.urls import re_path, path
from . import views

urlpatterns = [
    re_path(r'^$', views.Home.as_view(), name='Home_Page'),
    path('Details/<int:detail_id>', views.Details.as_view(), name='Item_Detail'),
    path('AddContact/<int:item_id>', views.AddContact.as_view(), name='Add'),
    path('Admin', views.ViewContact.as_view(), name='Admin'),
    path('login', views.UserLogin.as_view(), name='login'),
    path('logout', views.UserLogout.as_view(), name='logout'),
    path('Bokeh', views.BokehView.as_view(), name='Bokeh'),
]
