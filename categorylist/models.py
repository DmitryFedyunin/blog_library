from django.db import models

class Category(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/category'
