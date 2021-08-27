from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('mainlistmaterials.urls')),
    path('material/', include('materials.urls')),
    path('tags/', include('tagslist.urls')),
    path('category/',include('categorylist.urls'))
]
