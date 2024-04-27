from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, Category, Cart


# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("category", "name", "price", "color", "created", "img_display")
    list_display_links = ("name",)

    prepopulated_fields = {"slug": ("name",)}

    def img_display(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" height="100" />')

    img_display.short_description = 'Rasm'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "img_display")

    prepopulated_fields = {"slug": ("name",)}

    def img_display(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" height="100" />')

    img_display.short_description = 'Rasm'


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity')

    list_display_links = ("user", )
