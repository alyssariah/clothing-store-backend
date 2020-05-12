from django.db import models
from apps.authentication.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    pictureUrl = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100, choices=[('Dresses', 'Dresses'), ('Tops', 'Tops'), ('Bottoms', 'Bottoms'), ('Necklaces', 'Necklaces'), ('Bracelets', 'Bracelets'), ('Earrings', 'Earrings'), ('Sale', 'Sale'),])


    def __str__(self):
        return self.name

class CartItem(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    qty = models.IntegerField(default=1)
    size = models.CharField(max_length=100, choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ])
    ordered = models.BooleanField(default=False)




    def __str__(self):
        return f'{self.product}'


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField()


    class Meta:
        verbose_name_plural = 'Orders'

