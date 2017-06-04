import datetime
from unicodedata import decimal

from django.utils import timezone
from rest_framework import views, permissions, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response

from project.apps.goods.models import Goods, LastGoods
from project.apps.goods.serializers import GoodsSerializer


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return


class ApiGoodsView(views.APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def get(self, request):
        last_goods = LastGoods.objects.filter(
            created__gte=timezone.now() - datetime.timedelta(minutes=2),
        ).order_by('-id').first()

        if not last_goods:
            return Response({}, status.HTTP_200_OK)

        return Response({
            'id': last_goods.id,
            'name': last_goods.goods.name,
            'code': last_goods.goods.code,
            'description': last_goods.goods.description,
            'image': last_goods.goods.image,
            'cost': last_goods.weight * last_goods.goods.cost,
            'cost_goods': last_goods.goods.cost,
            'weight': last_goods.weight,
            'created': last_goods.created + datetime.timedelta(hours=7),
            'children': GoodsSerializer(last_goods.goods.children, many=True).data,
            'parent': last_goods.goods.parent_id
        }, status=status.HTTP_200_OK)

        # def post(self, request):
        #     code = request.data.get('code', None)
        #     weight = request.data.get('weight', 0)
        #
        #     print('+-'*20)
        #     print('code =', code)
        #     print('weight =', weight)
        #     print('+-'*20)
        #
        #     goods = Goods.objects.get(code=code)
        #
        #     LastGoods.objects.create(
        #         goods=goods,
        #         weight=weight
        #     )
        #
        #     return Response(status=status.HTTP_200_OK)


class ApiPostGoodsView(views.APIView):
    def get(self, request):
        code = request.GET.get('code', None)
        weight = request.GET.get('weight', 0)

        print('+-' * 20)
        print('code =', code)
        print('weight =', weight)

        # last_goods = LastGoods.objects.filter(
        #     created__gte=timezone.now() - datetime.timedelta(seconds=5),
        # ).order_by('-id').first()

        # if last_goods and decimal(last_goods.weight) == weight and last_goods.goods.code == code:
        #     print('copy')
        #     return Response(status=status.HTTP_200_OK)

        print('+-' * 20)
        goods = Goods.objects.get(code=code)

        LastGoods.objects.create(
            goods=goods,
            weight=weight,
            is_bought=request.GET.get('is_bought', False)
        )

        return Response(status=status.HTTP_200_OK)


class ApiListGoodsView(views.APIView):
    def get(self, request):
        goods = LastGoods.objects.filter(
            is_bought=True,
            created__gte=timezone.now() - datetime.timedelta(minutes=60)
        ).order_by('-id')[:10]

        r_goods = []

        for g in goods:
            r_goods.append({
                'id': g.id,
                'name': g.goods.name,
                'description': g.goods.description,
                'image': g.goods.image,
                'cost': g.weight * g.goods.cost,
                'cost_goods': g.goods.cost,
                'weight': g.weight,
                'created': g.created + datetime.timedelta(hours=7)
            })

        return Response(r_goods, status=status.HTTP_200_OK)
