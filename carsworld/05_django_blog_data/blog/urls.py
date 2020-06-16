from django.conf.urls import url
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from blog.views import CategoryViewSet, PostViewSet

schema_view = get_swagger_view(title='Blog API View')

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('post', PostViewSet)

urlpatterns = [
    url('docs/', schema_view)
]

urlpatterns += router.urls
