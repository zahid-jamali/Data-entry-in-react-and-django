from rest_framework.serializers import ModelSerializer
from . import models


class mySerializer(ModelSerializer):

    class Meta:
        model=models.Clients
        fields="__all__"

