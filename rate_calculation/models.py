from django.db import models


class Date(models.Model):
    date = models.DateField()
    cargo = models.CharField(max_length=100)
    rate = models.FloatField()

    def __str__(self):
        return str(self.date), self.cargo


