from django.db import models

# Create your models here.
class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publushed = models.DateTimeField("date published")

    def __str__(self):
        return self.title