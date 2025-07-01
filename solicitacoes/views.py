from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import HorarioDisponivel, Solicitacao
from .serializers import HorarioDisponivelSerializer, SolicitacaoSerializer
from .forms import SolicitacaoForm
from django.utils import timezone
from veiculos.models import Veiculo
from django.http import JsonResponse
from datetime import time
from motoristas.models import Motorista
from django.views.decorators.http import require_GET

@login_required
def solicitar_veiculo(request):
    if request.method == 'POST':
        form = SolicitacaoForm(request.POST)
        if form.is_valid():
            solicitacao = form.save(commit=False)
            solicitacao.usuario = request.user
            solicitacao.save()
            messages.success(request, 'Solicitação criada com sucesso!')
            return redirect('solicitacoes:list')
        else:
            messages.error(request, 'Por favor, corrija os erros no formulário.')
    else:
        form = SolicitacaoForm()
    
    context = {
        'form': form,
        'titulo': 'SOLICITAÇÃO DE TRANSPORTE INSTITUCIONAL'
    }
    return render(request, 'solicitar.html', context)

@login_required
def aprovar_solicitacao(request, pk):
    if not request.user.is_staff:
        messages.error(request, 'Apenas administradores podem aprovar solicitações')
        return redirect('solicitacoes:list')
    
    solicitacao = get_object_or_404(Solicitacao, pk=pk)
    if solicitacao.status != 'PENDENTE':
        messages.error(request, 'Solicitação já foi processada')
        return redirect('solicitacoes:list')
    
    solicitacao.status = 'APROVADA'
    solicitacao.aprovado_por = request.user
    solicitacao.data_aprovacao = timezone.now()
    solicitacao.save()
    
    messages.success(request, 'Solicitação aprovada com sucesso!')
    return redirect('solicitacoes:list')

@login_required
def cancelar_solicitacao(request, pk):
    if not request.user.is_staff:
        messages.error(request, 'Apenas administradores podem cancelar solicitações')
        return redirect('solicitacoes:list')
    
    solicitacao = get_object_or_404(Solicitacao, pk=pk)
    if solicitacao.status != 'PENDENTE':
        messages.error(request, 'Solicitação já foi processada')
        return redirect('solicitacoes:list')
    
    solicitacao.status = 'CANCELADA'
    solicitacao.save()
    
    messages.success(request, 'Solicitação cancelada com sucesso!')
    return redirect('solicitacoes:list')

class HorarioDisponivelViewSet(viewsets.ModelViewSet):
    queryset = HorarioDisponivel.objects.all()
    serializer_class = HorarioDisponivelSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['data', 'motorista']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        data = self.request.query_params.get('data')
        if data:
            queryset = queryset.filter(data=data, disponivel=True)
        return queryset

class SolicitacaoViewSet(viewsets.ModelViewSet):
    queryset = Solicitacao.objects.all()
    serializer_class = SolicitacaoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'veiculo', 'motorista']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            queryset = queryset.filter(usuario=self.request.user)
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if not request.user.is_staff:
            return Response(
                {'detail': 'Apenas administradores podem aprovar solicitações'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().update(request, *args, **kwargs)

@login_required
def home(request):
    if request.user.is_staff:
        # Para administradores, mostrar estatísticas e todas as solicitações
        total_solicitacoes = Solicitacao.objects.count()
        solicitacoes_pendentes = Solicitacao.objects.filter(status='PENDENTE').count()
        solicitacoes_aprovadas = Solicitacao.objects.filter(status='APROVADA').count()
        solicitacoes = Solicitacao.objects.all().select_related('usuario', 'veiculo', 'horario__motorista')
        context = {
            'total_solicitacoes': total_solicitacoes,
            'solicitacoes_pendentes': solicitacoes_pendentes,
            'solicitacoes_aprovadas': solicitacoes_aprovadas,
            'solicitacoes': solicitacoes,
        }
        return render(request, 'dashboard.html', context)
    else:
        # Para usuários comuns, mostrar suas solicitações
        solicitacoes = Solicitacao.objects.filter(usuario=request.user)
        context = {
            'solicitacoes': solicitacoes
        }
        return render(request, 'dashboard.html', context)

@login_required
def solicitacoes_list(request):
    if request.user.is_staff:
        # Para administradores, mostrar todas as solicitações
        solicitacoes = Solicitacao.objects.all().select_related('usuario', 'veiculo', 'horario__motorista')
    else:
        # Para usuários comuns, mostrar apenas suas solicitações
        solicitacoes = Solicitacao.objects.filter(usuario=request.user).select_related('veiculo', 'horario__motorista')
    
    context = {
        'solicitacoes': solicitacoes
    }
    return render(request, 'solicitacoes/list.html', context)

@require_GET
def horarios_livres(request):
    data = request.GET.get('data')
    horarios_comerciais = [time(h, 0) for h in range(8, 18)]
    horarios_livres = []
    motoristas = Motorista.objects.all()

    for horario in horarios_comerciais:
        # Para cada motorista, verifica se ele está livre nesse horário/data
        livre = False
        for motorista in motoristas:
            conflito = Solicitacao.objects.filter(
                data_realizacao=data,
                hora_saida=horario,
                horario__motorista=motorista
            ).exists()
            if not conflito:
                livre = True
                break
        if livre:
            horarios_livres.append(f'{horario.strftime("%H:%M")}')

    return JsonResponse({'horarios': horarios_livres})
