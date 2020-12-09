from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('sendInfo', views.submission),
    path('result', views.result),
]