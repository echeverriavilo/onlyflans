from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Flan, ContactForm, ContactFormModelForm, Testimonio
from django.urls import reverse
from .forms import ContactFormForm, TestimonioForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flanes': flanes_publicos})


def about(request):
    return render(request, 'about.html')

@login_required
def welcome(request):
    nombre_usuario = request.session.get('nombre', 'cliente')  
    flanes_privados = Flan.objects.filter(is_private=True)
    context = {
        'nombre': nombre_usuario,
        'flanes': flanes_privados
    }
    return render(request, 'welcome.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/exito')
    else:
        form = ContactFormModelForm()
    return render(request, 'contact.html', {'form': form})

def success(request):
    return render(request, 'success.html', {'message': 'Gracias por contactarte con OnlyFlans, te responderemos en breve.'})

def testimonios(request):
    testimonios = Testimonio.objects.all()
    paginator = Paginator(testimonios, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(page_obj.paginator.num_pages)
    
    if request.method == 'POST' and request.user.is_authenticated:
        form = TestimonioForm(request.POST)
        if form.is_valid():
            testimonio = form.save(commit=False)
            testimonio.usuario = request.user
            testimonio.save()
            return redirect('testimonios')
    else:
        form = TestimonioForm()
    return render(request, 'testimonios.html', {'page_obj': page_obj, 'form': form})
