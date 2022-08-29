from rest_framework.serializers import ModelSerializer

from core.models import Categoria, Ano, Marca, Modelo

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"

class AnoSerializer(ModelSerializer):
    class Meta:
        model = Ano
        fields = "__all__"

class ModeloSerializer(ModelSerializer):
    class Meta:
        model = Modelo
        fields = "__all__"