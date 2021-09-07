from django.urls import path
from rest_framework import routers 
from .views import champViewSet

router = routers.DefaultRouter()
router.register('feedbackChamp', champViewSet)

urlpatterns = router.urls