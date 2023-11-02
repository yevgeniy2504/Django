from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=255, blank=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    discount = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='products', null=True, blank=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name



