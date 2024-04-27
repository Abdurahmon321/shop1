from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("cart/", views.cart, name="cart"),
    path("shop_detail/", views.shop_detail, name="shop_detail"),
    path("shop/", views.shop_1, name="shop"),
]
