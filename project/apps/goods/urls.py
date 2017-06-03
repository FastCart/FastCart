from django.conf.urls import url
from .api import *


urlpatterns = [
    url(r'^api/goods/', ApiGoodsView.as_view()),
    url(r'^api/post-goods/', ApiPostGoodsView.as_view()),
]
