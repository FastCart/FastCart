from django.db import models


class Goods(models.Model):
    name = models.CharField(max_length=40)
    code = models.CharField(max_length=40)
    description = models.TextField(max_length=400)
    cost = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    image = models.URLField(null=True, blank=True)
    parent = models.ForeignKey(
        'Goods', null=True, blank=True, related_name='children'
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class LastGoods(models.Model):
    goods = models.ForeignKey(Goods)
    weight = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True)
    is_bought = models.BooleanField(default=False)
