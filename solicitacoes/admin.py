from django.contrib import admin
from .models import HorarioDisponivel, Solicitacao

@admin.register(HorarioDisponivel)
class HorarioDisponivelAdmin(admin.ModelAdmin):
    list_display = ['data', 'hora_inicio', 'hora_fim', 'motorista', 'disponivel']
    list_filter = ['data', 'disponivel', 'motorista']
    search_fields = ['motorista__nome']
    ordering = ['data', 'hora_inicio']
    date_hierarchy = 'data'
    
    fieldsets = (
        ('Informações do Horário', {
            'fields': ('data', 'hora_inicio', 'hora_fim')
        }),
        ('Motorista', {
            'fields': ('motorista',)
        }),
        ('Disponibilidade', {
            'fields': ('disponivel',)
        }),
    )

@admin.register(Solicitacao)
class SolicitacaoAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'nome_solicitante', 'departamento', 'finalidade', 'data_realizacao', 
        'hora_saida', 'hora_retorno', 'status', 'data_solicitacao'
    ]
    list_filter = [
        'status', 'finalidade', 'tipo_veiculo', 'data_realizacao', 
        'data_solicitacao', 'departamento'
    ]
    search_fields = [
        'nome_solicitante', 'usuario__username', 'departamento', 'cep', 'destino_endereco', 
        'descricao_servico', 'chefia_imediata'
    ]
    readonly_fields = ['data_solicitacao', 'data_aprovacao']
    date_hierarchy = 'data_realizacao'
    
    fieldsets = (
        ('Informações do Solicitante', {
            'fields': ('usuario', 'nome_solicitante', 'departamento', 'ramal', 'chefia_imediata')
        }),
        ('Informações da Solicitação', {
            'fields': ('finalidade', 'tipo_veiculo', 'cep', 'destino_endereco', 'descricao_servico')
        }),
        ('Data e Horários', {
            'fields': ('data_realizacao', 'hora_saida', 'hora_retorno')
        }),
        ('Observações', {
            'fields': ('observacoes',),
            'classes': ('collapse',)
        }),
        ('Sistema', {
            'fields': ('horario', 'veiculo', 'status', 'aprovado_por'),
            'classes': ('collapse',)
        }),
        ('Datas', {
            'fields': ('data_solicitacao', 'data_aprovacao'),
            'classes': ('collapse',)
        }),
    )
    
    def save_model(self, request, obj, form, change):
        if not change:  # Nova solicitação
            obj.usuario = request.user
        super().save_model(request, obj, form, change) 