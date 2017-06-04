from django.contrib import admin
from .models import *


class GoodsAdmin(admin.ModelAdmin):
    fields = (
        'name', 'code', 'description',
        'image', 'parent', 'cost', 'created',
    )
    list_display = ('name', 'code', 'cost', 'created',)
    list_filter = ('created',)
    readonly_fields = ('created',)
    search_fields = ('name', 'description',)

admin.site.register(Goods, GoodsAdmin)


class LastGoodsAdmin(admin.ModelAdmin):
    fields = ('goods', 'weight', 'created',)
    list_display = ('goods', 'weight', 'created',)
    list_filter = ('created',)
    readonly_fields = ('created',)

admin.site.register(LastGoods, LastGoodsAdmin)
