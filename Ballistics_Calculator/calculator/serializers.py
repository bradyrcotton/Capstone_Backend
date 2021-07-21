from rest_framework import serializers
from .models import Shooter,  Rifle, Dope


class ShooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shooter
        fields = ['id', 'userName', 'password']


class RifleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rifle
        fields = ['id', 'caliber', 'scopeAdjustment', 'ammoWeight', 'barrelLength', 'currentZero', 'windSpeed',
                  'boreToSight', 'shotAngle', 'rifleName', 'shooter']


class DopeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dope

        fields = ['id', 'caliber', 'scopeAdjustment', 'distance', 'currentZero', 'shooter']
