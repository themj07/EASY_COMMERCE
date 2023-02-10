from django.db import models 

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='articles/')
    
    status = models.BooleanField(default= True)
    date_add = models.DateTimeField(auto_now= True)
    date_update = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField()
    
    status = models.BooleanField(default= True)
    date_add = models.DateTimeField(auto_now= True)
    date_update = models.DateTimeField(auto_now= True)
    
    def __str__(self) :
        return self.name

class Reply(models.Model):
    nom = models.CharField(max_length=255)
    message = models.TextField()
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    
    status = models.BooleanField(default= True)
    date_add = models.DateTimeField(auto_now= True)
    date_update = models.DateTimeField(auto_now= True)
    
    def __str__(self) :
        return self.nom
    

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    facebook_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    photo = models.ImageField(upload_to='team_photos/')
    description = models.TextField()
    
    status = models.BooleanField(default= True)
    date_add = models.DateTimeField(auto_now= True)
    date_update = models.DateTimeField(auto_now= True)

    
    def __str__(self) :
        return self.name


class Contact(models.Model) :
    nom = models.CharField(max_length=150 )
    email = models.EmailField()
    commentaire = models.TextField()
    
    status = models.BooleanField(default= True)
    date_add = models.DateTimeField(auto_now= True)
    date_update = models.DateTimeField(auto_now= True)
    
    def __str__(self) :
        return self.nom



