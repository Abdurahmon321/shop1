from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Categoriya")
    img = models.ImageField(upload_to="category/")
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="Nomi")
    description = models.TextField(verbose_name="Izoh")
    img = models.ImageField(upload_to="product/")
    price = models.FloatField(verbose_name="narxi")
    color = models.CharField(max_length=50)
    discount = models.FloatField(null=True, blank=True, verbose_name="chegirma")
    slug = models.SlugField(unique=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username}'s Cart"
