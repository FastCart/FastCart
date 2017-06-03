import datetime
from django.utils import timezone

from rest_framework import views, permissions, status
from rest_framework.response import Response

from project.apps.goods.models import Goods, LastGoods
from rest_framework.authentication import SessionAuthentication


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return


class ApiGoodsView(views.APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def get(self, request):
        last_goods = LastGoods.objects.filter(
            created__gte=timezone.now() - datetime.timedelta(minutes=2)
        ).order_by('-id').first()

        if not last_goods:
            return Response({}, status.HTTP_200_OK)

        return Response({
            'id': last_goods.id,
            'name': last_goods.goods.name,
            'description': last_goods.goods.description,
            'image': last_goods.goods.image,
            'cost': last_goods.weight * last_goods.goods.cost,
            'cost_goods': last_goods.goods.cost,
            'weight': last_goods.weight,
            'created': last_goods.created + datetime.timedelta(hours=7)
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

        print('+-'*20)
        print('code =', code)
        print('weight =', weight)
        print('+-'*20)

        goods = Goods.objects.get(code=code)

        LastGoods.objects.create(
            goods=goods,
            weight=weight
        )

        return Response(status=status.HTTP_200_OK)
