from django.urls import path

from . import views

urlpatterns = [
    path('form/', views.form, name='contact.form'),
    path('layout-extends/', views.layout_extends, name='contact.layout_extends'),
    path('', views.index, name='contact.index'),
]