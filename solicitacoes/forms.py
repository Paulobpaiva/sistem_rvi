from django import forms
from .models import Solicitacao
from django.utils import timezone
from datetime import time, timedelta

class SolicitacaoForm(forms.ModelForm):
    class Meta:
        model = Solicitacao
        fields = [
            'nome_solicitante',
            'departamento',
            'ramal',
            'finalidade',
            'tipo_veiculo',
            'cep',
            'destino_endereco',
            'descricao_servico',
            'data_realizacao',
            'hora_saida',
            'hora_retorno',
            'observacoes',
            'chefia_imediata'
        ]
        widgets = {
            'nome_solicitante': forms.TextInput(attrs={'class': 'form-control'}),
            'departamento': forms.TextInput(attrs={'class': 'form-control'}),
            'ramal': forms.TextInput(attrs={'class': 'form-control'}),
            'finalidade': forms.Select(attrs={'class': 'form-control'}),
            'tipo_veiculo': forms.Select(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control', 'id': 'cep', 'placeholder': '00000-000 (opcional)'}),
            'destino_endereco': forms.TextInput(attrs={'class': 'form-control', 'id': 'destino_endereco'}),
            'descricao_servico': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'data_realizacao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora_saida': forms.Select(attrs={'class': 'form-control', 'id': 'hora_saida'}),
            'hora_retorno': forms.TimeInput(attrs={'class': 'form-control', 'id': 'hora_retorno', 'readonly': 'readonly'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'chefia_imediata': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Criar opções de horário comercial (08:00 às 17:00)
        horarios_comerciais = []
        for hora in range(8, 18):  # 8 até 17
            horarios_comerciais.append((time(hora, 0), f'{hora:02d}:00'))
        
        self.fields['hora_saida'].choices = [('', 'Selecione um horário')] + horarios_comerciais
    
    def clean_data_realizacao(self):
        data_realizacao = self.cleaned_data.get('data_realizacao')
        if data_realizacao and data_realizacao < timezone.now().date():
            raise forms.ValidationError('A data de realização não pode ser no passado.')
        return data_realizacao
    
    def clean_cep(self):
        cep = self.cleaned_data.get('cep')
        if cep:
            # Remover caracteres não numéricos
            cep = ''.join(filter(str.isdigit, cep))
            if len(cep) != 8:
                raise forms.ValidationError('CEP deve conter 8 dígitos.')
        return cep
    
    def clean(self):
        cleaned_data = super().clean()
        hora_saida = cleaned_data.get('hora_saida')
        hora_retorno = cleaned_data.get('hora_retorno')
        
        if hora_saida and hora_retorno and hora_saida >= hora_retorno:
            raise forms.ValidationError('A hora de retorno deve ser posterior à hora de saída.')
        
        return cleaned_data 