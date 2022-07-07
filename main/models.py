from django.db import models


class Object(models.Model):
    name = models.CharField(max_length=25, blank=True, null=True)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name
