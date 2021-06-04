from django.db import models


class Shooter(models.Model):
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Rifle(models.Model):
    caliber = models.IntegerField(default=30)
    scopeAdjustment = models.IntegerField(default=4)
    ammoWeight = models.IntegerField(default=150)
    barrelLength = models.IntegerField(default=26)
    currentZero = models.IntegerField(default=100)
    windSpeed = models.IntegerField(default=0)
    boreToSight = models.IntegerField(default=2)
    shotAngle = models.IntegerField(default=0)
    shooter = models.ForeignKey('calculator.Shooter', default=None, null=True, on_delete=models.CASCADE)

class Dope(models.Model):
    caliber = models.IntegerField(default=30)
    scopeAdjustment = models.IntegerField(default=4)
    distance = models.IntegerField(default=30)
    currentZero = models.IntegerField(default=100)
    shooter = models.ForeignKey('calculator.Shooter', default=None, null=True, on_delete=models.CASCADE)
