from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import Product

"""
from .forms import RawProductForm
def product_create_view(request):
    my_form = RawProductForm()
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)

    context = {"form": my_form}
    return render(request, "products/product_create.html", context)

"""

from .forms import ProductForm

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context = {'form': form}
    return render(request, "products/product_create.html", context)


def home_view(request, *args, **kwargs):
    context = {
        "my_text": "This is about us",
        "my_number": 123
    }
    return render(request, "home.html", context)

def product_list_view(request):
    queryset = Product.objects.all()
    context = {"object_list": queryset}
    return render(request, "products/product_list.html", context)