from rest_framework import serializers
from .models import programmer


class programmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = programmer
        # fields = ['fullname', 'laguaje', 'is_active'] se puede traer cualquier atributo del modelo
        fields = '__all__'  # con all nos traemos todos los atributos del modelo
