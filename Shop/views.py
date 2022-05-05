from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact
from math import ceil
from django.utils import timezone
# Create your views here.


def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))

    allprod = []
    catprods = Product.objects.values('category')
    # print(catprods)
    cats = {items['category'] for items in catprods}
    # print(cats)
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        # print(prod)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allprod.append([prod, range(1, nSlides), nSlides])
    # params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
    params = {'allprod': allprod}
    return render(request, 'Shop\index2.html', params)


def about(request):
    return render(request, "Shop\About.html")


def contact(request):
    if request.method == "POST":
        print(request)
        name = request.POST.get('name', 'default')
        email = request.POST.get('email', 'default')
        phone = request.POST.get('phone', 'default')
        country = request.POST.get('country', 'default')
        state = request.POST.get('state', 'default')
        massage = request.POST.get('massage', 'default')
        contact = Contact(name=name, email=email, phone=phone, country=country, state=state, massage=massage, datetime=timezone.now())
        contact.save()
    return render(request, "Shop\contact.html")


def search(request):
    return HttpResponse("hello Search")


def cart(request):
    return render(request, "Shop\cart.html")


def track(request):
    return HttpResponse("hello Track here")


def productView(request, prod_id):
    curr_product = Product.objects.filter(Product_id=prod_id)
    # print(curr_product)
    param = {'product': curr_product}
    return render(request, "Shop\Product_page2.html", param)