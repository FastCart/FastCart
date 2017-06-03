from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('project.apps.goods.urls')),
    url(r'^history/$', TemplateView.as_view(template_name='history.html')),
    url(r'', TemplateView.as_view(template_name='index.html')),
]
