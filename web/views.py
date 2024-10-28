from django.shortcuts import render

def index(request):
    return render(request, 'web/index.html', {'content': 'índice'})

def about(request):
    return render(request, 'web/about.html', {'content': 'acerca'})

def welcome(request):
    return render(request, 'web/welcome.html', {'content': 'bienvenido cliente'})
