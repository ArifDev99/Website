from django.db import models

# Create your models here.
from django.utils import timezone


class Product(models.Model):
    Product_id = models.AutoField(primary_key=True)
    Product_name = models.CharField(max_length=20, default=" ")
    category = models.CharField(max_length=20, default="")
    description = models.CharField(max_length=300, default=" ")
    Product_price = models.IntegerField(default="0")
    publish_date = models.DateField(default=timezone.now)
    Product_image = models.ImageField(upload_to="Shop/images", default="")

    def __str__(self):
        return self.Product_name


class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, default="")
    email = models.EmailField(default="")
    phone = models.IntegerField(default="")
    country = models.CharField(max_length=30, default="")
    state = models.CharField(max_length=30, default="")
    massage = models.CharField(max_length=30, default="")
    datetime = models.DateTimeField(timezone.now())

    def __str__(self):
        return self.name