from django.urls import path
from . import views

urlpatterns = [
    path('add', views.create, name='add_materials'),
    path('<int:pk>', views.MaterialView.as_view(), name='view_materials'),
    path('<int:pk>/update', views.MaterialUpdate.as_view(), name='update_materials'),
    path('<int:pk>/delete', views.MaterialDelete.as_view(), name='delete_materials'),
]
