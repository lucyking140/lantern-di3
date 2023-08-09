from rest_framework import serializers
from .models import Profiles

class ldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = ('user', 'follows')
