from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):
    """
    Stores a single post in the blog app.
    """
    title = models.CharField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")