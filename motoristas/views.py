from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Motorista
from .forms import MotoristaForm

def motoristas_list(request):
    motoristas = Motorista.objects.all()
    return render(request, 'motoristas/list.html', {'motoristas': motoristas})

def motorista_create(request):
    if request.method == 'POST':
        form = MotoristaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Motorista cadastrado com sucesso!')
            return redirect('motoristas:list')
    else:
        form = MotoristaForm()
    return render(request, 'motoristas/form.html', {'form': form})

def motorista_update(request, pk):
    motorista = get_object_or_404(Motorista, pk=pk)
    if request.method == 'POST':
        form = MotoristaForm(request.POST, instance=motorista)
        if form.is_valid():
            form.save()
            messages.success(request, 'Motorista atualizado com sucesso!')
            return redirect('motoristas:list')
    else:
        form = MotoristaForm(instance=motorista)
    return render(request, 'motoristas/form.html', {'form': form})

def motorista_delete(request, pk):
    motorista = get_object_or_404(Motorista, pk=pk)
    if request.method == 'POST':
        motorista.delete()
        messages.success(request, 'Motorista excluído com sucesso!')
        return redirect('motoristas:list')
    return render(request, 'motoristas/confirm_delete.html', {'motorista': motorista})
