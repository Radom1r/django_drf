from django.urls import path

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
]

from rest_framework import routers 
from .views import SensorViewSet, MeasurementViewSet

router = routers.SimpleRouter()
router.register(r'sensors', SensorViewSet)
router.register(r'measurements', MeasurementViewSet)

urlpatterns = router.urls