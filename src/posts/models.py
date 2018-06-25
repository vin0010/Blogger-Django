from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    content = models.TextField()

    def __str__(self):
        return self.title
