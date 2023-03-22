from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()

router.register('api/personas', ProjectViewSet, 'personas')

urlpatterns = router.urls