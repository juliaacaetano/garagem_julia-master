from django.contrib import admin

from core.models import Categoria, Marca, Modelo, Ano

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Ano)
