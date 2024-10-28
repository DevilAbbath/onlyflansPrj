from django.shortcuts import render, redirect
from .models import Flan
from .form import ContactFormForm



def index(request):
    flanes = Flan.objects.filter(is_private=False)
    return render(request, 'web/index.html', {'flanes': flanes})

def about(request):
    return render(request, 'web/about.html', {'content': 'acerca'})

def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'web/welcome.html', {'flanes': flanes_privados})

def contact(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exito')
    else:
        form = ContactFormForm()
    return render(request, 'web/contact.html', {'form': form})
