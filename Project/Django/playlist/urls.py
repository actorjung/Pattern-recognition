#[앱이름]/urls.py

from django.urls import path

from . import views

app_name = 'playlist'

urlpatterns = [
    path('', views.home,name = 'home'),
    path('playlist', views.playlist, name='playlist')
]