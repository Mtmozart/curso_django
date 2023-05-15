from django.shortcuts import render

def index(request):
    print(dir(request.user))
    print(f"User: {request.user}")

    if str(request.user) == 'AnonymousUser':
        test = 'Usuário não logado'
    else:
        test = 'Usuário logado'
    context = {
        'curso': 'Apredendo progamação web com django framework',
        'outro': 'Esse aqui parece ser muito legal',
        'logado': test
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')

