from django.db import models
from django.contrib.auth.models import User 


# Create your models here.


#

class Users(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    bio  = models.TextField(blank=True)
    image = models.ImageField(upload_to='userimages' , default='pp.png',blank=True)
    phone = models.CharField(max_length=100 , blank=True )
    cin =  models.CharField(max_length=100 , blank=True )
    city = models.CharField(max_length=100 , blank=True )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.username




class Post(models.Model):
    host = models.ForeignKey(User,on_delete=models.CASCADE)
    image =  models.ImageField(upload_to='postimages',default='avatar.png')
    description =  models.TextField(blank=True,default='Description...')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return self.description


class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[0:50]


class ChatMsg(models.Model):
    body = models.TextField()
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender')
    reciever = models.ForeignKey(User,on_delete=models.CASCADE,related_name='reciever')
    seen = models.BooleanField()

    def __str__(self):
        return self.body[0:50]


