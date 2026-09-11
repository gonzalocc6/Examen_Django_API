# API RESTful - Sistema de Gestión de Biblioteca

## Descripción
API RESTful completa desarrollada con Django 5 y Django REST Framework para el control y administración integral de una biblioteca. El sistema implementa las operaciones CRUD (incluyendo actualizaciones parciales con PATCH) para los modelos de Autores, Libros, Préstamos y Usuarios.

La API cuenta con seguridad basada en tokens (TokenAuthentication), restricción de permisos (IsAuthenticated) para proteger los recursos y generación automática de documentación técnica bajo el estándar OpenAPI 3.0 mediante Swagger UI y Redoc.

## Requisitos
- Python 3.10
- Django 5.0
- Django REST Framework 3.14
- drf-spectacular
- PostgreSQL

## Tecnologías y Librerías Utilizadas
- Django: Framework base del proyecto.
- Django REST Framework (DRF): Construcción de endpoints, serializadores y controladores mediante ModelViewSet.
- rest_framework.authtoken: Sistema de autenticación e intercambio de credenciales por Tokens.
- drf-spectacular: Generación e integración de esquemas OpenAPI 3.0 para Swagger y Redoc.
- psycopg2-binary: Conector/adaptador para la base de datos PostgreSQL.
- Postman: Herramienta para el diseño, pruebas de peticiones HTTP y validación de la API.

## Estructura de Entidades (Modelos)
- User: Gestión de usuarios y superusuarios del sistema para la obtención de tokens de acceso.
- Autor: Registro de datos de autores (nombre, nacionalidad, biografía).
- Libro: Información bibliográfica, stock y vinculación con autor.
- Prestamo: Control de salida y retorno de libros vinculados a usuarios con fechas de préstamo y devolución.

## Instalación y Configuración Local
1. Clonar el repositorio:
git clone https://github.com/gonzalocc6/sis_biblioteca_libros_Django.git

2. Crear entorno virtual:
python -m venv entorno
entorno\Scripts\activate

3. Instalar dependencias:
pip install django djangorestframework psycopg2-binary drf-spectacular

4. Ejecutar migraciones:
python manage.py migrate

5. Crear superusuario:
python manage.py createsuperuser

6. Iniciar servidor:
python manage.py runserver

## Autor
Gonzalo Cruz

## Licencia