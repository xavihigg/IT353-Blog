from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.urls import reverse

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def get_absolute_url(self):
        return reverse("home")
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
		
class Login(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=128)
