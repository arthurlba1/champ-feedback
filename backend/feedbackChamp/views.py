from .models import champs
from .serializers import ChampSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class champViewSet(ModelViewSet):
    queryset = champs.objects.all()
    serializer_class = ChampSerializer