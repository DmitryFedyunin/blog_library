from django.urls import path
from . import views

urlpatterns = [
    path('', views.tags_view, name='tags'),
    path('add', views.create_tags, name='create_tags'),
    path('<int:pk>', views.TagsView.as_view(), name='tags_view'),
    path('<int:pk>/delete', views.TagsDelete.as_view(), name='delete_tags'),
    path('<int:pk>/update', views.TagsUpdate.as_view(), name='update_tags'),
]
