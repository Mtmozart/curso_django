from django.shortcuts import render
#Biblioteca para gerar a página 404
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
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
    # prod = Product.objects.get(id=pk)
    prod =get_object_or_404(Product, id=pk)
    context = {
        'product': prod
    }
    return render(request, 'product.html', context)

def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf-8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf-8', status=500)
