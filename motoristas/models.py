from django.db import models
from django.utils import timezone

class Motorista(models.Model):
    STATUS_CHOICES = [
        ('ATIVO', 'Ativo'),
        ('INATIVO', 'Inativo')
    ]
    
    nome = models.CharField('Nome completo', max_length=100)
    cpf = models.CharField('CPF', max_length=11, unique=True)
    telefone = models.CharField('Telefone', max_length=15)
    status = models.CharField('Status', max_length=8, choices=STATUS_CHOICES, default='ATIVO')
    data_cadastro = models.DateTimeField('Data de cadastro', auto_now_add=True)
    
    class Meta:
        verbose_name = 'Motorista'
        verbose_name_plural = 'Motoristas'
        ordering = ['nome']
    
    def __str__(self):
        return self.nome
