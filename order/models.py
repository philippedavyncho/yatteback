from django.db import models
from shop.models import Produit 

        
class Order(models.Model):
    
    nom = models.CharField(max_length=255)
    
    phone = models.CharField(max_length=10)
    
    produit = models.ForeignKey(Produit, related_name='produit', on_delete=models.CASCADE)
    
    quantity = models.IntegerField(default=1)
    
    
    
    def __str__(self):
        
        return f"nom:{self.produit.name} quantité:{self.quantity} prix:{self.produit.price*self.quantity}"
        
        

    
        
    
    
    
