from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "fath/all_products.html")


def cart(request):
    return render(request, "cart/cart.html")


def shop_detail(request):
    return render(request, "shop_detail/shop_detail.html")


def shop_1(request):
    return render(request, "shop_1/shop.html")
