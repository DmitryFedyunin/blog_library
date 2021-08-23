from django.db import models

class Tags(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/tags'