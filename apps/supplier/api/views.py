from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.supplier.models import Supplier, SupplierSubsidiary, SupplierProduct
from .serializers import (
    SupplierSerializer, SupplierSubsidiarySerializer,
    SupplierProductSerializer,

)


class SupplierAPIView(APIView):
    def get_object(self, pk):
        try:
            return Supplier.objects.get(pk=pk)
        except Supplier.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        supplier_id = self.get_object(pk)
        serializer = SupplierSerializer(supplier_id)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        supplier_id = self.get_object(pk)
        serializer = SupplierSerializer(supplier_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        supplier_id = self.get_object(pk)
        supplier_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SupplierAPIListView(APIView):
    def get(self, request, format=None):
        supplier = Supplier.objects.all()
        serializer = SupplierSerializer(supplier, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SupplierSubsidiaryAPIView(APIView):
    def get_object(self, pk):
        try:
            return SupplierSubsidiary.objects.get(pk=pk)
        except SupplierSubsidiary.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        supplier_subsidiary_id = self.get_object(pk)
        serializer = SupplierSubsidiarySerializer(supplier_subsidiary_id)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        supplier_subsidiary_id = self.get_object(pk)
        serializer = SupplierSubsidiarySerializer(supplier_subsidiary_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        supplier_subsidiary_id = self.get_object(pk)
        supplier_subsidiary_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SupplierSubsidiaryAPIListView(APIView):
    def get(self, request, format=None):
        supplier_subsidiary = SupplierSubsidiary.objects.all()
        serializer = SupplierSubsidiarySerializer(supplier_subsidiary, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SupplierSubsidiarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SupplierProductAPIView(APIView):
    def get_object(self, pk):
        try:
            return SupplierProduct.objects.get(pk=pk)
        except SupplierProduct.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        supplier_product_id = self.get_object(pk)
        serializer = SupplierProductSerializer(supplier_product_id)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        supplier_product_id = self.get_object(pk)
        serializer = SupplierProductSerializer(supplier_product_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        supplier_product_id = self.get_object(pk)
        supplier_product_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SupplierProductAPIListView(APIView):
    def get(self, request, format=None):
        state = SupplierProduct.objects.all()
        serializer = SupplierProductSerializer(state, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SupplierProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SupplierProductSupplierAPIListView(APIView):
    def get(self, request, supplier, format=None):
        supplier_product = SupplierProduct.objects.filter(supplier=supplier)
        serializer = SupplierProductSerializer(supplier_product, many=True)
        return Response(serializer.data)