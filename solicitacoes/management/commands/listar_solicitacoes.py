from django.core.management.base import BaseCommand
from solicitacoes.models import Solicitacao

class Command(BaseCommand):
    help = 'Lista todas as solicitações do banco com campos principais'

    def handle(self, *args, **kwargs):
        solicitacoes = Solicitacao.objects.all()
        if not solicitacoes:
            self.stdout.write(self.style.WARNING('Nenhuma solicitação encontrada.'))
            return
        for s in solicitacoes:
            self.stdout.write(f'ID: {s.id} | Usuário: {s.usuario} | Data realização: {s.data_realizacao} | Status: {s.status} | Nome: {s.nome_solicitante}') 