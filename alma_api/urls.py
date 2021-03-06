from django.urls import path, include
from .views import orderlistView, genericOrderView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('order',orderlistView,basename='order')

urlpatterns = [
    path('viewset/', include(router.urls)),
    # path('order/',orderlistView.as_view())
    path('generic/view/', genericOrderView.as_view())
]