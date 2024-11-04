from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Flan
from .form import ContactFormForm
from .models import ContactForm



def index(request):
    flanes = Flan.objects.filter(is_private=False)
    return render(request, 'web/index.html', {'flanes': flanes})

def about(request):
    return render(request, 'web/about.html', {'content': 'acerca'})

def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'web/welcome.html', {'flanes': flanes_privados})

def contact(request):
    if request.method == "POST":
        form = ContactFormForm(request.POST)
        if form.is_valid():
            # Guardar los datos en el modelo
            ContactForm.objects.create(**form.cleaned_data)
            # Enviar una respuesta JSON para indicar éxito
            return JsonResponse({"success": True})
        else:
            # Enviar errores en caso de validación incorrecta
            return JsonResponse({"success": False, "errors": form.errors}, status=400)
    else:
        form = ContactFormForm()
    return render(request, "web/contact.html", {"form": form})