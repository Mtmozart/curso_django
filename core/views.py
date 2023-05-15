from django.shortcuts import render

def index(request):
    context = {
        'curso': 'Apredendo progamação web com django framework',
        'outro': 'Esse aqui parece ser muito legal'
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')

