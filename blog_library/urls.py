from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('mainlistmaterials.urls')),
    path('material/', include('materials.urls')),
    # path('material/', include('materials.urls'))
]
