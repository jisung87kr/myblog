from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title