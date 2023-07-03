from django.urls import path
from detectme import views
from django.conf import settings
from django.conf.urls.static import static

#TEMPLATE TAGGING
app_name = 'detectme'

urlpatterns = [
    path('', views.detect, name='detect'),
    path('index/',views.index,name='index'),
    path('detectme/', views.detectme, name='detectme'),
    path('upload/', views.uploadFile, name="uploadFile"),
    path('result/', views.result, name="result"),
    path('playlist/', views.playlist, name="playlist"),
    path('home/', views.home, name="home"),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT
    )