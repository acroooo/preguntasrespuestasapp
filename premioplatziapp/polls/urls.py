from django.urls import path
from . import views

# urls for polls

urlpatterns = [
    path('', views.index, name='index'),
]