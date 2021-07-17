from django.urls import path, include
from rest_framework import routers

from djtest import views

router = routers.DefaultRouter(trailing_slash=False)
router.register('module', views.ModuleView)
router.register('api', views.ApiView)
router.register('nft', views.NftView)
# 上层路由
urlpatterns = [
    path('', include(router.urls)),
]
