from django.conf.urls import url, include
from .views import BalanceViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('data', BalanceViewset, basename='balance-data')

urlpatterns = [
    url('', include(router.urls)),
]