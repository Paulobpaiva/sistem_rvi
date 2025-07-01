from django.contrib import admin
from .models import Veiculo

@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ['placa', 'modelo', 'tipo', 'status', 'data_cadastro']
    list_filter = ['tipo', 'status', 'data_cadastro']
    search_fields = ['placa', 'modelo']
    ordering = ['placa']
    readonly_fields = ['data_cadastro']
    
    fieldsets = (
        ('Informações do Veículo', {
            'fields': ('placa', 'modelo', 'tipo')
        }),
        ('Status', {
            'fields': ('status',)
        }),
        ('Informações do Sistema', {
            'fields': ('data_cadastro',),
            'classes': ('collapse',)
        }),
    ) 