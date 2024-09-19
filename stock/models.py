from unicodedata import category, name
from urllib.request import ProxyDigestAuthHandler
from django.db import models
from django.forms import DateTimeField

# Create your models here.
category_chioce=(
    ('Electronics', 'Electronics'),
    ('phone', 'phone'),
    ('It Equipment', 'It Equipment'),
)

class Category(models.Model):
    name=models.CharField(max_length=50, blank=True, null=True)
    
    def str(self):
        return self.name
    
class Stock(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    item_name=models.CharField(max_length=50, blank=True, null=True)
    quantity=models.IntegerField(default='0', blank=True, null=True)
    receive_quantity=models.IntegerField(default='0', blank=True, null=True)
    receive_by=models.CharField(max_length=50, blank=True, null=True)
    issue_quantity=models.IntegerField(default='0', blank=True, null=True)
    issue_by=models.CharField(max_length=50, blank=True, null=True)
    issue_to=models.CharField(max_length=50, blank=True, null=True)
    phone=models.CharField(max_length=50, blank=True, null=True)
    created_by=models.CharField(max_length=50, blank=True, null=True)
    reorder_level=models.IntegerField(default='0', blank=True, null=True)
    last_updated=models.DateTimeField(auto_now_add=False,auto_now=True)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    def str(self):
        return self.item_name
    
    
class StockHistory(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    item_name=models.CharField(max_length=50, blank=True, null=True)
    quantity=models.IntegerField(default='0', blank=True, null=True)
    receive_quantity=models.IntegerField(default='0', blank=True, null=True)
    receive_by=models.CharField(max_length=50, blank=True, null=True)
    issue_quantity=models.IntegerField(default='0', blank=True, null=True)
    issue_by=models.CharField(max_length=50, blank=True, null=True)
    issue_to=models.CharField(max_length=50, blank=True, null=True)
    phone=models.CharField(max_length=50, blank=True, null=True)
    created_by=models.CharField(max_length=50, blank=True, null=True)
    reorder_level=models.IntegerField(default='0', blank=True, null=True)
    last_updated=models.DateTimeField(auto_now_add=False,auto_now=False, null=True)
    timestamp=models.DateTimeField(auto_now_add=False,auto_now=False, null=True)
    def str(self):
        return self.item_name
    
    
class Customer(models.Model):
    name=models.CharField(max_length=50, null=True)
    phone=models.CharField(max_length=50, null=True)
    email=models.CharField(max_length=50, null=True)
    date_creared=models.DateTimeField(auto_now_add=True,null=True)
    def str(self):
        return self.name
    
    
class Tag(models.Model):
    name=models.CharField(max_length=50, null=True)
    def str(self):
        return self.name
    
class Product(models.Model):
    CATEGORY=(
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door')
    )
    name=models.CharField(max_length=50, null=True)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=50, null=True, choices=CATEGORY)
    description=models.CharField(max_length=200, null=True, blank=True)
    date_creared=models.DateTimeField(auto_now_add=True,  null=True)
    tags=models.ManyToManyField(Tag)
    def str(self):
        return self.name
    


class Order(models.Model):
    STATUS=(
        ('Pending', 'Pending'),
        ('Out For Delivery', 'Out For Delivery'),
        ('Delivered', 'Delivered')
    )
    customer=models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product=models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_creared=models.DateTimeField(auto_now_add=True,  null=True)
    status=models.CharField(max_length=50, null=True, choices=STATUS)
