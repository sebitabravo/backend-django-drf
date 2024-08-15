# Proyecto de Backend con Django y Django REST Framework

Este es un proyecto desarrollado en el marco de una asignatura universitaria, con el objetivo de aprender a utilizar Django junto con Django REST Framework para construir una API REST.

## Tabla de Contenidos
- [Proyecto de Backend con Django y Django REST Framework](#proyecto-de-backend-con-django-y-django-rest-framework)
  - [Tabla de Contenidos](#tabla-de-contenidos)
  - [Descripción](#descripción)
  - [Requisitos](#requisitos)
  - [Instalación](#instalación)
  - [Uso](#uso)
  - [Estructura del Proyecto](#estructura-del-proyecto)
  - [Endpoints](#endpoints)

## Descripción
Este proyecto es un ejemplo de una API RESTful creada con Django y Django REST Framework (DRF). Permite gestionar [describe brevemente lo que hace tu API, por ejemplo, "una lista de tareas", "una base de datos de usuarios", etc.].

## Requisitos
- Python 3.12.4
- Django 5.1
- Django REST Framework 3.15.2

## Instalación
1. Clona el repositorio:
```bash
git clone 
cd backend-django-drf
```

2. Crea un entorno virtual e instala las dependencias:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

4. Realiza las migraciones:
```bash
python manage.py migrate
```

5. Crea un superusuario:
```bash
python manage.py createsuperuser
```

6. Ejecuta el servidor:
```bash
python manage.py runserver
```

## Uso

Después de iniciar el servidor, puedes acceder a la API en http://localhost:8000/admin/. Utiliza herramientas como Postman o cURL para interactuar con los endpoints.

## Estructura del Proyecto

La estructura del proyecto es la siguiente:

```plaintext
backend-django-drf/
│
├── .venv/              # Entorno virtual (ignorado en Git)
├── api/                # Aplicación principal de Django
├── drf/                # Carpeta de configuraciones de Django
├── db.sqlite3          # Base de datos SQLite
├── manage.py           # Script principal de Django
└── requirements.txt    # Archivo de dependencias
```

## Endpoints

Aquí puedes listar y describir los principales endpoints de tu API.

	•	GET /api/items/ - Lista todos los ítems
	•	POST /api/items/ - Crea un nuevo ítem
	•	GET /api/items/{id}/ - Detalles de un ítem específico
	•	PUT /api/items/{id}/ - Actualiza un ítem específico
	•	DELETE /api/items/{id}/ - Elimina un ítem específico