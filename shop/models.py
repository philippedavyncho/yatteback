from django.db import models

# Create your models here.

class Categorie(models.Model):
    
    nom = models.CharField(max_length=255)
    slug = models.SlugField()
    
    def __str__(self):
        
        return self.nom



class Produit(models.Model):
    
    categorie = models.ForeignKey(Categorie, related_name='produit', on_delete=models.CASCADE)
    
    name = models.CharField(max_length=255)
    
    price = models.IntegerField()
    
    pribarrer = models.IntegerField(blank=True, default=0)
    
    description = models.TextField()
    
    texte = models.TextField(blank=True) 
    
    image = models.ImageField(upload_to='')
    
    logo = models.ImageField(upload_to='', blank=True, null=True)
    
    
    def __str__(self):
        
        return self.name