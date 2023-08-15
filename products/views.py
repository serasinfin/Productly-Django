from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect

from .forms import ProductForm
from .models import Product

# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(
        request,
        'index.html',
        context={'products': products}
    )

def products_details(request, product_id):
    # try:
    #     product = Product.objects.get(id=product_id)
        
    #     return render(
    #         request,
    #         'products_details.html',
    #         context={'product': product}
    #     )
    # except Product.DoesNotExist:
    #     raise Http404()
    product = get_object_or_404(Product, id=product_id)

    return render(
        request,
        'products_details.html',
        context={'product': product}
    )

def form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/products')
    else:
        form = ProductForm()

    return render(
        request,
        'product_form.html',
        {'form': form}
    )
