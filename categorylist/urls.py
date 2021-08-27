from django.urls import path
from . import views


urlpatterns = [
    path('',views.category_view, name='category_view'),
    path('add', views.create_category, name='category_create'),
    path('<int:pk>', views.CategoryViews.as_view(), name='category_view'),
    path('<int:pk>/delete',views.CategoryDelete.as_view(), name='category_delete'),
    path('<int:pk>/update', views.CategoryUpdate.as_view(), name='category_update')
]