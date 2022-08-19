from django.db import models
from .category import Category

class Product(models.Model):
    product_name =models.CharField(max_length=30)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    product_price =models.IntegerField(default=0)
    product_detail =models.TextField()
    product_image =models.ImageField(upload_to='media')