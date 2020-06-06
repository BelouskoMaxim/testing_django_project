from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list', views.list, name='list'),
    path('detail/<int:id>', views.detail, name='detail'),
]