from django.contrib import admin
from .models import Motorista

@admin.register(Motorista)
class MotoristaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'telefone', 'status', 'data_cadastro']
    list_filter = ['status', 'data_cadastro']
    search_fields = ['nome', 'cpf', 'telefone']
    ordering = ['nome']
    readonly_fields = ['data_cadastro']
    
    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('nome', 'cpf', 'telefone')
        }),
        ('Status', {
            'fields': ('status',)
        }),
        ('Informações do Sistema', {
            'fields': ('data_cadastro',),
            'classes': ('collapse',)
        }),
    ) 

# Customização do Django Admin
admin.site.site_header = 'Administração RVI'
admin.site.site_title = 'Administração RVI'
admin.site.index_title = 'Bem-vindo à Administração RVI' 