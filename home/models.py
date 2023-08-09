from django.db import models
from django.contrib.auth.models import User

class Reports(models.Model):
    """
    Stores a single report in the home app.
    """
    title = models.CharField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reports")
    report_img = models.ImageField(upload_to="images/", default="default.png", null=True)
    img_caption = models.CharField(max_length=200, default="Credit")
    admin_approved = models.BooleanField(default=False)