from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Product, Category, Supplier
from .forms import ProductForm

def index(request):
    products = Product.objects.all()[:3]  # featured products
    return render(request, 'index.html', {'products': products})

def list_products(request):
    products = Product.objects.all()
    price = request.GET.get('price')
    category = request.GET.get('category')
    supplier = request.GET.get('supplier')
    if price:
        products = products.filter(Price__lte=price)
    if category:
        products = products.filter(Category__catName__icontains=category)
    if supplier:
        products = products.filter(Suppliers__suppName__icontains=supplier)
    return render(request, 'list_products.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_products')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def view_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'view_product.html', {'product': product})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('list_products')
    return render(request, 'delete_product.html', {'product': product})

def search_categories(request):
    if request.method == 'POST':
        query = request.POST.get('q')
        if query:
            categories = Category.objects.filter(catName__icontains=query)
            suppliers = Supplier.objects.filter(suppName__icontains=query)
            results = []
            for cat in categories:
                results.append(f"Category: {cat.catName} - {cat.product_set.count()} products")
            for supp in suppliers:
                results.append(f"Supplier: {supp.suppName} - {supp.product_set.count()} products")
        else:
            results = []
        return render(request, 'search_results.html', {'results': results})
    else:
        return render(request, 'search.html')
