from rest_framework import serializers
from .models import Shooter,  Rifle


class ShooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shooter
        fields = ['userName', 'password']


class RifleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rifle
        fields = ['caliber', 'scopeAdjustment', 'ammoWeight', 'barrelLength', 'currentZero', 'windSpeed',
                  'boreToSight', 'shotAngle', 'shooter']

