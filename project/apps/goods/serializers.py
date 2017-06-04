from rest_framework import serializers

from project.apps.goods.models import Goods


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = (
            'id', 'name', 'code', 'description',
            'image', 'cost', 'created',
        )
