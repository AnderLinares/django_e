from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Currency, ExchangeRate, ProductBrand, ProductModel, VehicleBrand, VehicleModel
from .serializers import (
    CurrencySerializer, ExchangeRateSerializer,
    ProductBrandSerializer, ProductModelSerializer,
    VehicleBrandSerializer, VehicleModelSerializer)


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


class ProductBrandAPIView(APIView):
    def get_object(self, pk):
        try:
            return ProductBrand.objects.get(pk=pk)
        except ProductBrand.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        brand_id = self.get_object(pk)
        serializer = ProductBrandSerializer(brand_id)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        brand_id = self.get_object(pk)
        serializer = ProductBrandSerializer(brand_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        brand_id = self.get_object(pk)
        brand_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductBrandAPIListView(APIView):
    def get(self, request, format=None):
        brand = ProductBrand.objects.all()
        serializer = ProductBrandSerializer(brand, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductBrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductModelAPIView(APIView):
    def get_object(self, pk):
        try:
            return ProductModel.objects.get(pk=pk)
        except ProductModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        model_id = self.get_object(pk)
        serializer = ProductModelSerializer(model_id)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        model_id = self.get_object(pk)
        serializer = ProductModelSerializer(model_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        model_id = self.get_object(pk)
        model_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductModelAPIListView(APIView):
    def get(self, request, format=None):
        model = ProductModel.objects.all()
        serializer = ProductModelSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductModelBrandAPIListView(APIView):
    def get(self, request, brand, format=None):
        product_model = ProductModel.objects.filter(brand=brand)
        serializer = ProductModelSerializer(product_model, many=True)
        return Response(serializer.data)



class VehicleBrandAPIView(APIView):
    def get_object(self, pk):
        try:
            return VehicleBrand.objects.get(pk=pk)
        except VehicleBrand.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        brand_id = self.get_object(pk)
        serializer = VehicleBrandSerializer(brand_id)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        brand_id = self.get_object(pk)
        serializer = VehicleBrandSerializer(brand_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        brand_id = self.get_object(pk)
        brand_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VehicleBrandAPIListView(APIView):
    def get(self, request, format=None):
        brand = VehicleBrand.objects.all()
        serializer = VehicleBrandSerializer(brand, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VehicleBrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VehicleModelAPIView(APIView):
    def get_object(self, pk):
        try:
            return VehicleModel.objects.get(pk=pk)
        except VehicleModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        model_id = self.get_object(pk)
        serializer = VehicleModelSerializer(model_id)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        model_id = self.get_object(pk)
        serializer = VehicleModelSerializer(model_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        model_id = self.get_object(pk)
        model_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VehicleModelAPIListView(APIView):
    def get(self, request, format=None):
        model = VehicleModel.objects.all()
        serializer = VehicleModelSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VehicleModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VehicleModelBrandAPIListView(APIView):
    def get(self, request, brand, format=None):
        vehicle_model = VehicleModel.objects.filter(brand=brand)
        serializer = VehicleModelSerializer(vehicle_model, many=True)
        return Response(serializer.data)