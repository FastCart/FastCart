from django.db import models


class Goods(models.Model):
    name = models.CharField(max_length=40)
    code = models.CharField(max_length=40)
    description = models.TextField(max_length=400)
    cost = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='goods/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
