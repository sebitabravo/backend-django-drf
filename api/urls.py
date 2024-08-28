from django.urls import path, include
from rest_framework import routers
from api import views

# Este elemento enrutador permite manejar multiples rutas.
router = routers.DefaultRouter()
# Esta es la base del conjunto de rutas o la raiz de las rutas.
# Aqui se maneja las rutas o ENDs points de la API.
router.register(r'programmers', views.programmerViewSet)
# la 'r' permite que no se interprete como un sato de linea o como un escape de caracter.es para que no tome los caracteres como \n o \t que es un salto de linea en formato RAW en python
# 'programmers' es el nombre de la ruta o END point.

urlpatterns = [
    path('', include(router.urls)),
    # la ruta base va a incluir todos los elementos que tengamos en el router creado en URLS.PY
    # esta es la lista de URLS que maneja ROUTER en sus elementos URLS.
]
