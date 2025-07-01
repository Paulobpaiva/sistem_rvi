from django.db import models
from django.conf import settings
from django.utils import timezone
from motoristas.models import Motorista
from veiculos.models import Veiculo

class HorarioDisponivel(models.Model):
    data = models.DateField('Data')
    hora_inicio = models.TimeField('Hora início')
    hora_fim = models.TimeField('Hora fim')
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE, verbose_name='Motorista')
    disponivel = models.BooleanField('Disponível', default=True)
    
    class Meta:
        verbose_name = 'Horário Disponível'
        verbose_name_plural = 'Horários Disponíveis'
        ordering = ['data', 'hora_inicio']
        unique_together = ['data', 'hora_inicio', 'hora_fim', 'motorista']
    
    def __str__(self):
        return f"{self.data} - {self.hora_inicio} até {self.hora_fim}"

class Solicitacao(models.Model):
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('APROVADA', 'Aprovada'),
        ('CANCELADA', 'Cancelada')
    ]
    
    FINALIDADE_CHOICES = [
        ('SERVICO_ADMINISTRATIVO', 'Serviço Administrativo'),
        ('SERVICO_CAMPO', 'Serviço de Campo'),
        ('AEROPORTO', 'Aeroporto'),
        ('OUTROS', 'Outros')
    ]
    
    TIPO_VEICULO_CHOICES = [
        ('CARRO', 'Carro'),
        ('MOTO', 'Moto'),
        ('UTILITARIO', 'Utilitário'),
        ('PICKUP', 'Pick up')
    ]
    
    # Informações do solicitante
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Solicitante')
    nome_solicitante = models.CharField('Nome do Solicitante', max_length=100)
    departamento = models.CharField('Departamento', max_length=100)
    ramal = models.CharField('Ramal', max_length=20)
    data_solicitacao = models.DateTimeField('Data da solicitação', auto_now_add=True)
    
    # Informações da solicitação
    finalidade = models.CharField('Finalidade da solicitação', max_length=30, choices=FINALIDADE_CHOICES)
    tipo_veiculo = models.CharField('Tipo de Veículo', max_length=15, choices=TIPO_VEICULO_CHOICES)
    cep = models.CharField('CEP', max_length=9, blank=True, help_text='Digite o CEP para carregar o endereço automaticamente (opcional)')
    destino_endereco = models.CharField('Destino/Endereço', max_length=200)
    descricao_servico = models.TextField('Descrição do serviço')
    data_realizacao = models.DateField('Data para realização do serviço')
    hora_saida = models.TimeField('Hora saída')
    hora_retorno = models.TimeField('Hora retorno (Previsão)')
    observacoes = models.TextField('Observações', blank=True)
    chefia_imediata = models.CharField('Chefia imediata', max_length=100)
    
    # Campos do sistema (relacionados ao horário e veículo)
    horario = models.ForeignKey(HorarioDisponivel, on_delete=models.CASCADE, verbose_name='Horário', null=True, blank=True)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, verbose_name='Veículo', null=True, blank=True)
    status = models.CharField('Status', max_length=10, choices=STATUS_CHOICES, default='PENDENTE')
    
    # Campos de aprovação
    aprovado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='solicitacoes_aprovadas',
        verbose_name='Aprovado por'
    )
    data_aprovacao = models.DateTimeField('Data de aprovação', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Solicitação'
        verbose_name_plural = 'Solicitações'
        ordering = ['-data_solicitacao']
    
    def __str__(self):
        return f"Solicitação #{self.pk} - {self.usuario.username} - {self.data_realizacao}"
    
    def save(self, *args, **kwargs):
        if self.status == 'APROVADA' and self.horario:
            self.horario.disponivel = False
            self.horario.save()
            self.data_aprovacao = timezone.now()
        elif self.status == 'CANCELADA' and self.horario:
            self.horario.disponivel = True
            self.horario.save()
        super().save(*args, **kwargs)
