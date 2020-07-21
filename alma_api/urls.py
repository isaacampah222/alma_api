from django.urls import path, include
from .views import orderlistView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('ordering',orderlistView,basename='ordering')

urlpatterns = [
    path('viewset/', include(router.urls)),
    # path('order/',orderlistView.as_view())
]