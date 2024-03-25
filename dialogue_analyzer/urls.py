from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_dialogue, name='upload_dialogue'),
]
