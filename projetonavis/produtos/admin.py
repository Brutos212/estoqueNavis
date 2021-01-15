from django.contrib import admin

from .models import Produtos

@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'importado',
        'ncm',
        'preco',
        'estoque',
        'estoque_minimo',
    )
    search_fields = ('produtos',)
    list_fields = ('importado',)
