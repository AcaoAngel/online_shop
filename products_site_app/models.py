from django.db import models

# Create your models here.

class Products(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=500)
    price=models.DecimalField(max_digits=11, decimal_places=2)
    picture=models.ImageField(upload_to="static/media/", null=True, blank=True, default="default_img.png")
    def __str__(self):
        return f"{self.name}, {self.price}"

class Cart_products(models.Model):
    product_id=models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    name=models.CharField(max_length=100, default="no-name")
    description=models.TextField(max_length=500, default="no-description")
    price=models.DecimalField(max_digits=11, decimal_places=2, default=0)
    picture=models.ImageField(upload_to="static/media/", null=True, blank=True, default="default_img.png")
    
