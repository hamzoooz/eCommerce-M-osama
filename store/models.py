from django.db import models
from datetime import datetime
import os
from django.contrib.auth.models import User
# from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField
# Create your models here.


def get_file_path_cat(request, filename):
    orifinal_filename = filename
    nowtime = datetime.now().strftime('%Y %d %h %M:%S')
    filename = '%s%s' % (nowtime, orifinal_filename)
    return os.path.join('upload/category', filename)


class Category(models.Model):
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=get_file_path_cat, null=True, blank=True, default='defualt-pic-avater.jpg')
    descrption = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False, help_text='0=default, 1 = hidden')
    trending = models.BooleanField(default=False, help_text='0=default, 1 = Trending')
    meta_tilte = models.CharField(max_length=150, null=False, blank=False)
    meta_keyword = models.CharField(max_length=150, null=False, blank=False)
    meta_description = models.CharField(max_length=150, null=False, blank=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


def get_file_path_prodcut(request, filename):
    orifinal_filename = filename
    name = 'bookhope.com'
    nowtime = datetime.now().strftime('%Y %d %h %M:%S')
    filename = '%s %s.png' % (orifinal_filename, name)
    return os.path.join('upload/product', filename)

class Product(models.Model):
    link = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    product_image = models.ImageField(upload_to=get_file_path_prodcut, null=True, blank=True)
    # content = models.TextField(max_length=500, null=False, blank=False)
    # descrption = RichTextField()
    content = RichTextField()
    small_descrption = models.TextField(max_length=1000, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    original_price = models.FloatField(null=False, blank=False)
    selling_price = models.FloatField(null=False, blank=False)
    status = models.BooleanField(default=False, help_text='0=default, 1 = hidden')
    trending = models.BooleanField(default=False, help_text='0=default, 1 = Trending')
    tags = models.CharField(max_length=150, blank=True, null=True)
    meta_tilte = models.CharField(max_length=150, null=False, blank=False)
    meta_keyword = models.CharField(max_length=150, null=False, blank=False)
    meta_description = models.CharField(max_length=150, null=False, blank=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Card(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,  on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,  on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=150, null=False)
    lname = models.CharField(max_length=150, null=False)
    email = models.EmailField(max_length=150, null=False)
    phone = models.CharField(max_length=150, null=False)
    # phone = models.PhoneNumberField()
    address = models.TextField()
    city = models.CharField(max_length=150, null=False)
    stats = models.CharField(max_length=150, null=False)
    conutry = models.CharField(max_length=150, null=False)
    pincode = models.CharField(max_length=150, null=False)
    total_price = models.FloatField(null=False)
    payment_mode = models.CharField(max_length=150, null=False)
    payment_id = models.CharField(max_length=150, null=False)
    order_status = (
        ('pending', 'pending'),
        ('out for Shipping', 'out for Shipping'),
        ('Completed', 'Completed'),
    )
    satuts = models.CharField(
        max_length=150, choices=order_status, default='pending')
    message = models.TextField(null=True)
    tracking_no = models.CharField(max_length=150, null=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"order for {self.id} , has email {self.email}   with {self.tracking_no}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)

    def __str__(self):
        return f"order for {self.order.id} , has email {self.order.email}   with {self.order.tracking_no}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # fname = models.CharField(max_length=150, null=False )
    # lname = models.CharField(max_length=150, null=False )
    # email = models.EmailField(max_length=150, null=False) 
    phone = models.CharField(max_length=150, null=False)
    address = models.TextField(null=False)
    city = models.CharField(max_length=150, null=False)
    stats = models.CharField(max_length=150, null=False)
    conutry = models.CharField(max_length=150, null=False)
    pincode = models.CharField(max_length=150, null=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile for {self.user.username}"

class Whatsapp(models.Model):
    status = models.BooleanField(default=True)
    number = models.CharField(max_length=50, null=False, blank=False)
    message = models.TextField(max_length=500)
    width = models.CharField(max_length=50, null=False, blank=False)
    heigth = models.CharField(max_length=50, null=False, blank=False)
    icon = models.ImageField(upload_to=get_file_path_cat, null=True, blank=True, default='whatsapp-icon.png')

    def __str__(self):
        return self.message
        # return self.message[0:10]

class CarouselImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='carousel')
    caption = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title} {self.caption}"
        # return self.message[0:10]