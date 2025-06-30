from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
   
    username=models.TextField(null=False,unique=True)
    email=models.EmailField(unique=True,null=True)
    avathar=models.ImageField(null=True)
    
    
    def __str__(self):
        return self.username
    

    
class Rooms(models.Model):
    host=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(null=True,default="New room")
    
    created=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering=['-created']
    
    def __str__(self):
        return self.name
    
class Message(models.Model):
   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, null=True)
    

    sender = models.CharField(max_length=10)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        ordering=['-created']
        
    def __str__(self):
        return self.body[0:40]