from django.urls import path
from . import views

urlpatterns = [
    path('', views.AudioView.as_view(), name='record')
]
