from rest_framework import serializers
from .models import Profissional, Consulta

class ProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = '__all__'
    def validate_contato(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("O campo contato deve conter apenas números. ")
        if len(value) != 11:  # Exemplo para validar número de telefone com 11 dígitos
            raise serializers.ValidationError("O campo contato deve conter 11 dígitos.")
        return value
        
    

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'
