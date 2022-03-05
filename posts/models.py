from django.db import models
import uuid

"""
Model which represent a post
"""
class Post(models.Model):
    uuid4 = models.CharField(max_length=50, unique=True, default = uuid.uuid4, null=False)
    created_at = models.DateField(auto_now_add=True, null=False)
    title = models.CharField(max_length=255, null=False, unique=True)
    subtitle = models.CharField(max_length=255, null=False, unique=True)
    author = models.CharField(max_length=255, null=True)
    content = models.TextField(null=True)
    
    