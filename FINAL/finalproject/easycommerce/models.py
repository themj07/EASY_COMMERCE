from django.db import models
from django.contrib.auth.models import User


class Produit(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='produits/')
    description = models.TextField()
    categorie = models.CharField(max_length=255)
    
    status = models.BooleanField(default= True)
    date_add = models.DateTimeField(auto_now= True)
    date_update = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.name
    
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name="product_order")
    quantity = models.PositiveIntegerField(default=1)
    prix_total = models.PositiveIntegerField(default=0)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(null=True, blank=True)
    
    
    def __str__(self) :
        return f"{self.user.username}({self.quantity})"
    


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ManyToManyField(Cart)
    prix_total = models.PositiveIntegerField(default=0)
    
