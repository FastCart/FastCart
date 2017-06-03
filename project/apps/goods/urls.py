from django.conf.urls import url
from .api import *


urlpatterns = [
    url(r'^api/goods/', ApiGoodsView.as_view()),
]
