# from .forms import MyModelAdminForm
# from .models import Product
from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Card)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Profile)
admin.site.register(Whatsapp)
admin.site.register(CarouselImage)


# @admin.register(Product)
# class MyModelAdmin(admin.ModelAdmin):
#     form = MyModelAdminForm
