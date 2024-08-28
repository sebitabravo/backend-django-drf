# Proyecto de Backend con Django y Django REST Framework

Este proyecto ha sido desarrollado como parte de una asignatura universitaria, con el objetivo de aprender a utilizar Django y Django REST Framework para construir una API REST.

## Tabla de Contenidos

- [Proyecto de Backend con Django y Django REST Framework](#proyecto-de-backend-con-django-y-django-rest-framework)
  - [Tabla de Contenidos](#tabla-de-contenidos)
  - [Descripción](#descripción)
  - [Requisitos](#requisitos)
  - [Instalación](#instalación)
  - [Uso](#uso)
  - [Estructura del Proyecto](#estructura-del-proyecto)

## Descripción

Este proyecto es un ejemplo de una API RESTful creada con Django y Django REST Framework (DRF).

## Requisitos

- Python: 3.11.1 o superior
- Django: 5.1 o superior
- Django: REST Framework 3.15.2 o superior

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/sebitabravo/backend-django-drf.git
cd backend-django-drf
```

2. Crea un entorno virtual e instala las dependencias:

### Importante ves que inicien el proyecto tienen que inicar el 'source .venv/bin/activate'

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Realiza las migraciones:

- Con esto creamos la base de datos SQLite y se realiza la migracion a la base de datos necesaria.

```bash
python3 manage.py migrate
```

5. Crea un superusuario para acceder al panel de administración:

```bash
python3 manage.py createsuperuser
```

Ejemplo de credenciales para el superusuario:

- Usuario: profe
- Email: nonemail@example.com
- Contraseña: 123456 (La contraseña aparecerá como insegura, pero puedes continuar ingresando 'y').

6. Ejecuta el servidor de desarrollo::

```bash
python3 manage.py runserver
```

## Uso

Después de iniciar el servidor, puedes acceder a las siguientes rutas en tu navegador:

- https://127.0.0.1:8000/ - Página de inicio.
- https://127.0.0.1:8000/admin/ - Panel de administración de Django.
- https://127.0.0.1:8000/api/ - Punto de entrada para la API.

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

## Documentación Adicional

Para más detalles y configuraciones avanzadas, consulta la documentación oficial de [Django REST Framework](https://www.django-rest-framework.org/).
