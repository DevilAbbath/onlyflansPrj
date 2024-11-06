from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Flan, Comentary
from .form import ContactFormForm, ComentaryForm
from .models import ContactForm


def index(request):
    flanes = Flan.objects.filter(is_private=False)
    return render(request, 'web/index.html', {'flanes': flanes})

def about(request):
    return render(request, 'web/about.html', {'content': 'acerca'})

@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'web/welcome.html', {'flanes': flanes_privados , 'username': request.user.username})

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

@login_required
def flan_detail(request, flan_id):
    flan = get_object_or_404(Flan, id = flan_id)
    comentaries = flan.comentaries.all()
    
    if request.method == 'POST':
        form = ComentaryForm(request.POST)
        if form.is_valid():
            comentary = form.save(commit = False)
            comentary.user = request.user
            comentary.flan = flan
            comentary.save()
            return redirect('flan_detail', flan_id = flan.id)
    else:
        form = ComentaryForm()
        
    return render(request, 'web/flan_detail.html', {
        'flan': flan,
        'comentaries': comentaries,
        'form': form
    })