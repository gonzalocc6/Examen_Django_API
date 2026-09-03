from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from biblioteca.views import AutorViewSet, LibroViewSet, PrestamoViewSet

# Configuración del Router de DRF
router = DefaultRouter()
router.register(r'autores', AutorViewSet)
router.register(r'libros', LibroViewSet)
router.register(r'prestamos', PrestamoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rutas CRUD de la API
    path('api/', include(router.urls)),

    # Endpoint para autenticarse y obtener el Token
    path('api/login/', obtain_auth_token, name='api_token_auth'),
]