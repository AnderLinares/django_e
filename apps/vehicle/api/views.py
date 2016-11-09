from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.vehicle.models import Vehicle
from .serializers import (
    VehicleSerializer

)


class VehicleAPIView(APIView):
    def get_object(self, pk):
        try:
            return Vehicle.objects.get(pk=pk)
        except Vehicle.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        vehicle_id = self.get_object(pk)
        serializer = VehicleSerializer(vehicle_id)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        vehicle_id = self.get_object(pk)
        serializer = VehicleSerializer(vehicle_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        vehicle_id = self.get_object(pk)
        vehicle_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VehicleAPIListView(APIView):
    def get(self, request, format=None):
        vehicle = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicle, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

