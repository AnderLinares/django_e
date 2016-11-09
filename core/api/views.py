from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import (
    Currency, ExchangeRate, ProductBrand, ProductModel, VehicleBrand, VehicleModel,
    VehicleEnrollment,
    Labour, LabourCategory, HandWorkCategory, HandWork)
from .serializers import (
    CurrencySerializer, ExchangeRateSerializer,
    ProductBrandSerializer, ProductModelSerializer,
    VehicleBrandSerializer, VehicleModelSerializer, VehicleEnrollmentSerializer, LabourCategorySerializer,
    LabourSerializer, HandWorkCategorySerializer, HandWorkSerializer)


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


class VehicleEnrollmentAPIView(APIView):
    def get_object(self, pk):
        try:
            return VehicleEnrollment.objects.get(pk=pk)
        except VehicleEnrollment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        vehicle_enrollment_id = self.get_object(pk)
        serializer = VehicleEnrollmentSerializer(vehicle_enrollment_id)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        vehicle_enrollment_id = self.get_object(pk)
        serializer = VehicleEnrollmentSerializer(vehicle_enrollment_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        vehicle_enrollment_id = self.get_object(pk)
        vehicle_enrollment_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VehicleEnrollmentAPIListView(APIView):
    def get(self, request, format=None):
        vehicle_enrollment = VehicleEnrollment.objects.all()
        serializer = VehicleEnrollmentSerializer(vehicle_enrollment, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VehicleEnrollmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LabourCategoryAPIView(APIView):
    def get_object(self, pk):
        try:
            return LabourCategory.objects.get(pk=pk)
        except LabourCategory.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        labour_category_id = self.get_object(pk)
        serializer = LabourCategorySerializer(labour_category_id)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        labour_category_id = self.get_object(pk)
        serializer = LabourCategorySerializer(labour_category_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        labour_category_id = self.get_object(pk)
        labour_category_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LabourCategoryAPIListView(APIView):
    def get(self, request, format=None):
        labour_category = LabourCategory.objects.all()
        serializer = LabourCategorySerializer(labour_category, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LabourCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LabourAPIView(APIView):
    def get_object(self, pk):
        try:
            return Labour.objects.get(pk=pk)
        except Labour.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        labour_id = self.get_object(pk)
        serializer = LabourSerializer(labour_id)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        labour_id = self.get_object(pk)
        serializer = LabourSerializer(labour_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        labour_id = self.get_object(pk)
        labour_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LabourAPIListView(APIView):
    def get(self, request, format=None):
        labour = Labour.objects.all()
        serializer = LabourSerializer(labour, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LabourSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LabourCategoryLabourAPIView(APIView):
    def get(self, request, labour_category, format=None):
        labour_model = Labour.objects.filter(labour_category=labour_category)
        serializer = LabourSerializer(labour_model, many=True)
        return Response(serializer.data)




class HandWorkCategoryAPIView(APIView):
    def get_object(self, pk):
        try:
            return HandWorkCategory.objects.get(pk=pk)
        except HandWorkCategory.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        handwork_category_id = self.get_object(pk)
        serializer = HandWorkCategorySerializer(handwork_category_id)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        handwork_category_id = self.get_object(pk)
        serializer = HandWorkCategorySerializer(handwork_category_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        handwork_category_id = self.get_object(pk)
        handwork_category_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class HandWorkCategoryAPIListView(APIView):
    def get(self, request, format=None):
        handwork_category = HandWorkCategory.objects.all()
        serializer = HandWorkCategorySerializer(handwork_category, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HandWorkCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HandWorkAPIView(APIView):
    def get_object(self, pk):
        try:
            return HandWork.objects.get(pk=pk)
        except HandWork.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        handwork_id = self.get_object(pk)
        serializer = HandWorkSerializer(handwork_id)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        handwork_id = self.get_object(pk)
        serializer = HandWorkSerializer(handwork_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        handwork_id = self.get_object(pk)
        handwork_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class HandWorkAPIListView(APIView):
    def get(self, request, format=None):
        handwork = HandWork.objects.all()
        serializer = HandWorkSerializer(handwork, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HandWorkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HandWorkCategoryHandWorkAPIView(APIView):
    def get(self, request, handworkcategory, format=None):
        handwork_model = HandWork.objects.filter(handwork_category_id=handworkcategory)
        serializer = HandWorkSerializer(handwork_model, many=True)
        return Response(serializer.data)