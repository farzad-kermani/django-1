from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE)

    
    def __str__(self):
        return self.title
    
    def  get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])
    