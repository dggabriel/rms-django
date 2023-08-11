from django.urls import path
from . import views
from django.conf import settings
 
urlpatterns = [
    path('', views.getAssetClasses),
    path('api/get/', views.getAssetClasses),
    path('api/post/', views.postAssetClasses),
]
