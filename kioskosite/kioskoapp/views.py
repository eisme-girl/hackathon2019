from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import PerfilForm,TagForm
# Create your views here.
@login_required
def index(request):
    return render(request, 'kioskoapp/index.html')
@login_required   
def agregar_perfil(request):
    if request.method == "POST":
        form = PerfilForm(request.POST)
        form.instance.usuario = request.user
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'kioskoapp/agregar_perfil.html', {'form': form})
    else:
        form = PerfilForm()
        return render(request, 'kioskoapp/agregar_perfil.html', {'form': form})

@login_required
def agregar_tag(request):
    return render(request, 'kioskoapp/index.html')