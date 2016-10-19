from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.zone.models import Zone, Country, State
from .serializers import (
    ZoneSerializer, CountrySerializer, StateSerializer
)


class ZoneAPIView(APIView):
    def get_object(self, pk):
        try:
            return Zone.objects.get(pk=pk)
        except Zone.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        zone_id = self.get_object(pk)
        serializer = ZoneSerializer(zone_id)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        zone_id = self.get_object(pk)
        serializer = ZoneSerializer(zone_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        zone_id = self.get_object(pk)
        zone_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ZoneAPIListView(APIView):
    def get(self, request, format=None):
        zone = Zone.objects.all()
        serializer = ZoneSerializer(zone, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ZoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CountryAPIView(APIView):
    def get_object(self, pk):
        try:
            return Country.objects.get(pk=pk)
        except Country.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        country_id = self.get_object(pk)
        serializer = CountrySerializer(country_id)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        country_id = self.get_object(pk)
        serializer = CountrySerializer(country_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        country_id = self.get_object(pk)
        country_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CountryAPIListView(APIView):
    def get(self, request, format=None):
        country = Country.objects.all()
        serializer = CountrySerializer(country, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CountryZoneAPIListView(APIView):
    def get(self, request, zone, format=None):
        country = Country.objects.filter(zone=zone)
        serializer = CountrySerializer(country, many=True)
        return Response(serializer.data)


class StateAPIView(APIView):
    def get_object(self, pk):
        try:
            return State.objects.get(pk=pk)
        except State.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        state_id = self.get_object(pk)
        serializer = StateSerializer(state_id)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        state_id = self.get_object(pk)
        serializer = StateSerializer(state_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        state_id = self.get_object(pk)
        state_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StateAPIListView(APIView):
    def get(self, request, format=None):
        state = State.objects.all()
        serializer = StateSerializer(state, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
