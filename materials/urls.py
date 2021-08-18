from django.urls import path
from . import views

urlpatterns = [
    path('add', views.create, name='add_materials'),
    path('view', views.view, name='view_materials'),
]
