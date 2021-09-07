from rest_framework.serializers import ModelSerializer
from .models import champs

class ChampSerializer(ModelSerializer):
    class Meta:
        model = champs
        fields = ['id', 'name', 'rating', 'comment']