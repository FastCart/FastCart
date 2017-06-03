from django.db import models


class Goods(models.Model):
    name = models.CharField(max_length=40)
    code = models.CharField(max_length=40)
    description = models.TextField(max_length=400)
    cost = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    image = models.URLField()
    created = models.DateTimeField(auto_now_add=True)


class LastGoods(models.Model):
    goods = models.ForeignKey(Goods)
    weight = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True)
