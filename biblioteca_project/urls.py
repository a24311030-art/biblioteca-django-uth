"""
URL configuration for biblioteca_project project.
"""

from django.contrib import admin
from django.urls import path, include  # ← AGREGAR 'include'
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('libros.urls')),  # ← AGREGAR ESTA LÍNEA
]

# Para servir archivos de media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)