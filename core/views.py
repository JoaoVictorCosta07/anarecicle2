from django.shortcuts import render, redirect
from .forms import ColetaForm
from django.http import HttpResponse
from .models import Coleta  # Importe seu modelo Coleta
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
    return render(request, 'recicle/pages/index.html')

def cadastro(request):
    if request.method == 'POST':
        form = ColetaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Sucesso, você pode voltar para a página inicial agora')
        else:
            return HttpResponse('ERRO')
    else:  
        form = ColetaForm()
    return render(request, 'recicle/pages/cadastro.html', {'form': form})

@login_required
def parceiros(request):
    if User.is_authenticated:
        coletas = Coleta.objects.all()  # Busca todos os registros do modelo Coleta
        return render(request, 'recicle/pages/parceiros.html', {'coletas': coletas})  # Renderiza o template 'parceiros.html'
    else:
        return redirect('/')
    

def dicas(request):
    return render(request, 'recicle/pages/dicas.html')