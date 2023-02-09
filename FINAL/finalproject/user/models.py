from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Contact(models.Model) :
    nom = models.CharField(max_length=150 )
    email = models.EmailField()
    commentaire = models.TextField()
    
    status = models.BooleanField(default= True)
    date_add = models.DateTimeField(auto_now= True)
    date_update = models.DateTimeField(auto_now= True)
    
    def __str__(self) :
        return self.nom
    
