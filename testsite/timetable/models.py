from django.db import models


class Training(models.Model):
    name = models.CharField(max_length=50)
    start = models.DateTimeField()

    def __str__(self):
        return self.name
