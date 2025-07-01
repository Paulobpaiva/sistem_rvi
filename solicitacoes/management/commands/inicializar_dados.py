from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import time
from motoristas.models import Motorista
from veiculos.models import Veiculo
from solicitacoes.models import HorarioDisponivel
import random

class Command(BaseCommand):
    help = 'Cria dados iniciais para o sistema'

    def handle(self, *args, **options):
        # Criar motoristas iniciais (se não existirem)
        if Motorista.objects.count() == 0:
            motoristas = [
                Motorista(
                    nome="João Silva",
                    cpf="12345678901",
                    telefone="(11) 99999-9999",
                    status="ATIVO"
                ),
                Motorista(
                    nome="Maria Santos",
                    cpf="98765432101",
                    telefone="(11) 88888-8888",
                    status="ATIVO"
                ),
            ]
            Motorista.objects.bulk_create(motoristas)
            self.stdout.write(self.style.SUCCESS('Motoristas criados com sucesso'))
        else:
            self.stdout.write(self.style.WARNING('Motoristas já existem'))

        # Criar veículos iniciais (se não existirem)
        if Veiculo.objects.count() == 0:
            veiculos = [
                Veiculo(
                    placa="ABC1234",
                    modelo="Fiat Uno",
                    tipo="CARRO",
                    status="DISPONIVEL"
                ),
                Veiculo(
                    placa="XYZ5678",
                    modelo="Honda CG",
                    tipo="MOTO",
                    status="DISPONIVEL"
                ),
            ]
            Veiculo.objects.bulk_create(veiculos)
            self.stdout.write(self.style.SUCCESS('Veículos criados com sucesso'))
        else:
            self.stdout.write(self.style.WARNING('Veículos já existem'))

        # Criar horários disponíveis para os próximos 7 dias (se não existirem)
        if HorarioDisponivel.objects.count() == 0:
            hoje = timezone.now().date()
            for dia in range(7):
                data = hoje + timezone.timedelta(days=dia)
                for motorista in Motorista.objects.filter(status="ATIVO"):
                    horarios = [
                        HorarioDisponivel(
                            data=data,
                            hora_inicio=time(hora, 0),
                            hora_fim=time(hora + 1, 0),
                            motorista=motorista,
                            disponivel=True
                        )
                        for hora in range(8, 18)  # Horários de 8h às 17h
                    ]
                    HorarioDisponivel.objects.bulk_create(horarios)
            self.stdout.write(self.style.SUCCESS('Horários criados com sucesso'))
        else:
            self.stdout.write(self.style.WARNING('Horários já existem'))
