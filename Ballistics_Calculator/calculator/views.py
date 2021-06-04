from django.shortcuts import render
from .models import Shooter, Rifle, Dope
from .serializers import ShooterSerializer, RifleSerializer, DopeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
# Create your views here.


class ShooterList(APIView):

    def get(self,request):
        shooter = Shooter.objects.all()
        serializer = ShooterSerializer(shooter, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ShooterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RifleList(APIView):

    def get(self, request):
        rifle = Rifle.objects.all()
        serializer = RifleSerializer(rifle, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RifleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RifleBuild(APIView):

    def get_object(self, request):
        try:
            rifle = Rifle.objects.filter(shooter_id=request)

            return rifle

        except Rifle.DoesNotExist:
            raise Http404

    def get(self, request,pk):
        rifle = self.get_object(pk)
        serializer = RifleSerializer(rifle)
        return Response(serializer.data)

    def put(self, request, pk):
        rifle = self.get_object(pk)
        serializer = RifleSerializer(rifle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        rifle = self.get_object(pk)
        rifle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DopeList(APIView):

    def get(self, request):
        dope = Dope.objects.all()
        serializer = DopeSerializer(dope, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DopeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        dope = self.get_object(pk)
        dope.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)