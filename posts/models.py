from django.db import models

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=60)
    post_content = models.TextField()
    published_date = models.DateTimeField(auto_now=True)