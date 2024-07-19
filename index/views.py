from django.shortcuts import render
from .models import Product, Category


# Create your views here.
def home_page(request):
    # Получаем данные из БД
    products = Product.objects.all()
    categories = Category.objects.all()

    # Передаем данные на фронт
    context = {'products': products,
               'categories': categories}
    return render(request, 'home.html', context)


def get_exact_pr(request, pk):
    exact_product = Product.objects.get(id=pk)

    # Передаем данные на фронт
    context = {'product': exact_product}
    return render(request, 'product.html', context)


def get_exact_category(request, pk):
    exact_category = Category.objects.get(id=pk)
    products = Product.objects.filter(pr_category=exact_category)

    # Передаем данные на фронт
    context = {'products': products}
    return render(request, 'category.html', context)
