from io import open_code
from django.db import models
from django.db.models import query
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.contrib import auth
from django.db.models.expressions import Case

from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey, ManyToManyField



class Post(models.Model):
    title=models.CharField(max_length=150)
    body=models.TextField()
    liked=models.IntegerField(default=0)
    
    creator = models.ForeignKey(User, on_delete=CASCADE)
    updated=models.DateField(auto_now=True)
    created=models.DateField(auto_now_add=True)
    cover=models.ImageField(blank=True, null=True)



    


    
    
    

    def __str__(self):
        return "{}".format(self.title)

class slider(models.Model):
    img1=models.ImageField()
    img2=models.ImageField(null=True,blank=True)
    img3=models.ImageField(null=True,blank=True)
    

class likee(models.Model):
    user_like=models.ForeignKey(User,on_delete=CASCADE,default=0)
    post=models.ForeignKey(Post,on_delete=CASCADE,default=None)


class Querry(models.Model):
    content=models.TextField()
    provider=models.ForeignKey(User,on_delete=CASCADE)
    post=models.ForeignKey(Post,on_delete=CASCADE, default=None)
    date_created=models.DateTimeField(auto_now_add=True,help_text="The date and time the Querry was created.")
    date_edited=models.DateTimeField(null=True,help_text="The date and time the Querry was last edited.")
    Answer=models.CharField(default=None,max_length=1000,null=True,blank=True)



    
    

    def __str__(self):
        return "{}".format(self.content)

    










    
