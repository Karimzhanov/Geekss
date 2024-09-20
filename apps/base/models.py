from django.db import models

# Create your models here.

from django.db import models

class LandingSection(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)  
    name = models.CharField(max_length=255,)
    description = models.TextField(blank=True, null=True)  

    def __str__(self):
        return self.title if self.title else f'Section {self.pk}'

class Post(models.Model):
    title = models.CharField(max_length=255)  
    content = models.TextField()  
    image = models.ImageField(upload_to='posts/images/', blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title
