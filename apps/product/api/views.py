from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.product.models import (
    ProductCategory, Product
)
from .serializers import (
    ProductCategorySerializer, ProductSerializer
)


class ProductCategoryAPIView(APIView):
    def get_object(self, pk):
        try:
            return ProductCategory.objects.get(pk=pk)
        except ProductCategory.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category_id = self.get_object(pk)
        serializer = ProductCategorySerializer(category_id)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        category_id = self.get_object(pk)
        serializer = ProductCategorySerializer(category_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        category_id = self.get_object(pk)
        category_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductCategoryAPIListView(APIView):
    def get(self, request, format=None):
        category = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(category, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductAPIView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product_id = self.get_object(pk)
        serializer = ProductSerializer(product_id)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product_id = self.get_object(pk)
        serializer = ProductSerializer(product_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product_id = self.get_object(pk)
        product_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductAPIListView(APIView):
    def get(self, request, format=None):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductCategoryCategoryAPIListView(APIView):
    def get(self, request, category, format=None):
        product = Product.objects.filter(product_category=category)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
