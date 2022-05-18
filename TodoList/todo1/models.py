from django.db import models

class List(models.Model):
    item = models.CharField(max_length=256)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.item} | {self.completed}"