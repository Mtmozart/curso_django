from django.shortcuts import render
from .models import Product
def index(request):
    products = Product.objects.all()
    print(dir(request.user))
    print(f"User: {request.user}")

    if str(request.user) == 'AnonymousUser':
        test = 'Usuário não logado'
    else:
        test = 'Usuário logado'
    context = {
        'curso': 'Apredendo progamação web com django framework',
        'outro': 'Esse aqui parece ser muito legal',
        'products': products,
        'logado': test
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')

def product(request, pk):
    prod = Product.objects.get(id=pk)
    context = {
        'product': prod
    }
    return render(request, 'product.html', context)

