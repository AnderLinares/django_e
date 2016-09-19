from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Currency, ExchangeRate
from .serializers import (
    CurrencySerializer, ExchangeRateSerializer
)


class CurrencyAPIView(APIView):
    def get_object(self, pk):
        try:
            return Currency.objects.get(pk=pk)
        except Currency.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        currency_id = self.get_object(pk)
        serializer = CurrencySerializer(currency_id)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        currency_id = self.get_object(pk)
        serializer = CurrencySerializer(currency_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        currency_id = self.get_object(pk)
        currency_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CurrencyAPIListView(APIView):
    def get(self, request, format=None):
        currency = Currency.objects.all()
        serializer = CurrencySerializer(currency, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CurrencySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExchangeRateAPIView(APIView):
    def get_object(self, pk):
        try:
            return ExchangeRate.objects.get(pk=pk)
        except ExchangeRate.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        exchangerate_id = self.get_object(pk)
        serializer = ExchangeRateSerializer(exchangerate_id)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        exchangerate_id = self.get_object(pk)
        serializer = ExchangeRateSerializer(exchangerate_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        exchangerate_id = self.get_object(pk)
        exchangerate_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ExchangeRateAPIListView(APIView):
    def get(self, request, format=None):
        exchangerate = ExchangeRate.objects.all()
        serializer = ExchangeRateSerializer(exchangerate, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExchangeRateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
