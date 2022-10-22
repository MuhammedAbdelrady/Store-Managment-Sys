from random import choices
from django.db import models

# Create your models here.
class Customer (models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name

class Tag (models.Model):
    name = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name

class Product (models.Model):
    STATUS=(( 'indoor', 'indoor'), 
            ('Out Door', 'Out Door')
        )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True , choices=STATUS)
    description = models.CharField(max_length=200, null=True , blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    #many to many relations
    tags=models.ManyToManyField(Tag)
    def __str__(self):
        return self.name

class Order(models.Model):
    #one to many relations
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    STATUS=(( 'Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered'))
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    stat = models.CharField(max_length=200, null=True, choices=STATUS)