from rest_framework import views, permissions, status
from rest_framework.response import Response

from project.apps.goods.models import Goods


class ApiGoodsView(views.APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request):
        goods = Goods.objects.get(code=request.data.get('code', None))
        weight = request.data.get('weight', 0)

        return Response({
            'name': goods.name,
            'description': goods.description,
            'name': goods.name,
            'cost': weight * goods.cost
        }, status=status.HTTP_200_OK)
