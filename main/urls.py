from django.urls import path
from .import views

urlpatterns = [
    path('createartist', views.createArtist),
    path('', views.index),
    path('success', views.success, name="success"),
    path('showartist', views.showArtist, name="showartist"),
]