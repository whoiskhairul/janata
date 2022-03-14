from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('load-data/', include('load_data.urls')),
    path('', include('visualization.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
