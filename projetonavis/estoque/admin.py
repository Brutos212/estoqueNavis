from django.contrib import admin

from .models import Estoque, EstoqueItens



class EstoqueItensInline(admin.TabularInline):
    model = EstoqueItens
    extra = 0

@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    inlines = (EstoqueItensInline,)
    list_display = ('__str__', 'nf')
    search_fields = ('nf',)
    #search_fields = ('Service Tag',)
    list_fields = ('funcionario',)
    date_hierarchy = 'created'
