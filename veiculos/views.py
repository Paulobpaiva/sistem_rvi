from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Veiculo
from .forms import VeiculoForm

def veiculos_list(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'veiculos/list.html', {'veiculos': veiculos})

def veiculo_create(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Veículo cadastrado com sucesso!')
            return redirect('veiculos:list')
    else:
        form = VeiculoForm()
    return render(request, 'veiculos/form.html', {'form': form})

def veiculo_update(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    if request.method == 'POST':
        form = VeiculoForm(request.POST, instance=veiculo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Veículo atualizado com sucesso!')
            return redirect('veiculos:list')
    else:
        form = VeiculoForm(instance=veiculo)
    return render(request, 'veiculos/form.html', {'form': form})

def veiculo_delete(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    if request.method == 'POST':
        veiculo.delete()
        messages.success(request, 'Veículo excluído com sucesso!')
        return redirect('veiculos:list')
    return render(request, 'veiculos/confirm_delete.html', {'veiculo': veiculo})
