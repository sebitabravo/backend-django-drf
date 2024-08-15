from django.contrib import admin
from .models import programmer

# Asemos visibles el modelo en panel de administración.
admin.site.register(programmer)
