# API RESTful - Sistema de Gestión de Biblioteca

## Descripción
API RESTful completa desarrollada con Django 5 y Django REST Framework para el control y administración integral de una biblioteca. El sistema implementa las operaciones CRUD (incluyendo actualizaciones parciales con `PATCH`) para los modelos de **Autores**, **Libros**, **Préstamos** y **Usuarios**.

La API cuenta con seguridad basada en tokens (`TokenAuthentication`), restricción de permisos (`IsAuthenticated`) para proteger los recursos y generación automática de documentación técnica bajo el estándar OpenAPI 3.0 mediante Swagger UI y Redoc.

## Requisitos
- Python 3.10+
- Django 5.0+
- Django REST Framework 3.14+
- drf-spectacular

## Tecnologías y Librerías Utilizadas
- **Django**: Framework base del proyecto.
- **Django REST Framework (DRF)**: Construcción de endpoints, serializadores y controladores mediante `ModelViewSet`.
- **`rest_framework.authtoken`**: Sistema de autenticación e intercambio de credenciales por Tokens.
- **`drf-spectacular`**: Generación e integración de esquemas OpenAPI 3.0 para Swagger y Redoc.
- **Postman**: Herramienta utilizada para el diseño, pruebas de integración y validación de respuestas de la API.

## Estructura de Entidades (Modelos)
- **User**: Gestión de usuarios y superusuarios del sistema para la obtención de tokens de acceso.
- **Autor**: Registro de datos de autores (nombre, nacionalidad, biografía).
- **Libro**: Información bibliográfica, stock y vinculación con autor.
- **Prestamo**: Control de salida y retorno de libros vinculados a usuarios con fechas de préstamo y devolución.

## Instalación y Configuración Local

## Comandos Git para Actualizar el Repositorio
# Paso 1: Verifica qué archivos has cambiado (como tu README.md).
git status

# Paso 2: Preparar y agregar los archivos que modificaste
git add .

# Paso 3: Guardar el paquete de cambios en tu historial local
git commit -m "Se actualiza el README.md y la documentación del proyecto"

# Paso 4: Subir tus cambios locales a GitHub
git push origin main
Autor:
gonzalo