from rest_framework.viewsets import ModelViewSet

from core.models import  Marca, Categoria, Modelo, Ano
from core.serializers import (
    MarcaSerializer,
    CategoriaSerializer,
    ModeloSerializer,
    AnoSerializer,
)

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer

class AnoViewSet(ModelViewSet):
    queryset = Ano.objects.all()
    serializer_class = AnoSerializer

    