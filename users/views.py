from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Encuesta, Respuesta, Informe, Evento
from .forms import RespuestaForm,InformeForm
from django.shortcuts import redirect

def encuestas(request):
    posts = Encuesta.objects.all()
    return render(request, 'encuestas.html', {'posts': posts})
def informar(request):
    posts = Informe.objects.all()
    return render(request, 'encuestas.html', {'posts': posts})
def evento(request):
    posts = Evento.objects.all()
    return render(request, 'encuestas.html', {'posts': posts})

def respuestas(request, pk):
    Encuestas = get_object_or_404(Encuesta, pk=pk)
    Respuestas = Respuesta.objects.all()
    return render(request, 'respuestas.html',{'Respuestas': Respuestas,'Encuestas': Encuestas})
    
def nuevarespuesta(request):
    if request.method == "POST":
        form = RespuestaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('encuestas')
    else:
        form = RespuestaForm()
    return render(request, 'nuevarespuesta.html', {'form': form})
def nuevoinforme(request):
    if request.method == "POST":
        form = InformeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.fechapub = timezone.now()
            post.save()
            return redirect('informar')
    else:
        form = InformeForm()
    return render(request, 'nuevarespuesta.html', {'form': form})

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'