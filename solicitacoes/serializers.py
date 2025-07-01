from rest_framework import serializers
from .models import HorarioDisponivel, Solicitacao
from motoristas.models import Motorista
from veiculos.models import Veiculo

class MotoristaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorista
        fields = ['id', 'nome', 'cpf', 'telefone', 'status']

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ['id', 'placa', 'modelo', 'tipo', 'status']

class HorarioDisponivelSerializer(serializers.ModelSerializer):
    motorista = MotoristaSerializer(read_only=True)
    
    class Meta:
        model = HorarioDisponivel
        fields = ['id', 'data', 'hora_inicio', 'hora_fim', 'motorista', 'disponivel']

class SolicitacaoSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField()
    horario = HorarioDisponivelSerializer()
    veiculo = VeiculoSerializer()
    aprovado_por = serializers.StringRelatedField()
    
    class Meta:
        model = Solicitacao
        fields = [
            'id', 'usuario', 'data_solicitacao', 'horario', 'veiculo', 'status',
            'observacoes', 'aprovado_por', 'data_aprovacao'
        ]
