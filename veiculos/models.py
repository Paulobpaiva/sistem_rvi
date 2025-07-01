from django.db import models
from django.utils import timezone

class Veiculo(models.Model):
    TIPO_CHOICES = [
        ('CARRO', 'Carro'),
        ('MOTO', 'Moto'),
        ('CAMINHAO', 'Caminhão')
    ]
    
    STATUS_CHOICES = [
        ('DISPONIVEL', 'Disponível'),
        ('INDISPONIVEL', 'Indisponível')
    ]
    
    placa = models.CharField('Placa', max_length=7, unique=True)
    modelo = models.CharField('Modelo', max_length=100)
    tipo = models.CharField('Tipo', max_length=10, choices=TIPO_CHOICES)
    status = models.CharField('Status', max_length=12, choices=STATUS_CHOICES, default='DISPONIVEL')
    data_cadastro = models.DateTimeField('Data de cadastro', auto_now_add=True)
    
    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'
        ordering = ['placa']
    
    def __str__(self):
        return f"{self.placa} - {self.modelo}"
