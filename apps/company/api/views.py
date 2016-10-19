from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.company.models import (
    Organization, Subsidiary, Correlative
)
from .serializers import (
    OrganizationSerializer, SubsidiarySerializer,
    CorrelativeSerializer
)


class OrganizationAPIView(APIView):
    def get_object(self, pk):
        try:
            return Organization.objects.get(pk=pk)
        except Organization.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        organization_id = self.get_object(pk)
        serializer = OrganizationSerializer(organization_id)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        organization_id = self.get_object(pk)
        serializer = OrganizationSerializer(organization_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        organization_id = self.get_object(pk)
        organization_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrganizationAPIListView(APIView):
    def get(self, request, format=None):
        organization = Organization.objects.all()
        serializer = OrganizationSerializer(organization, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubsidiaryAPIView(APIView):
    def get_object(self, pk):
        try:
            return Subsidiary.objects.get(pk=pk)
        except Subsidiary.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        subsidiary_id = self.get_object(pk)
        serializer = SubsidiarySerializer(subsidiary_id)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        subsidiary_id = self.get_object(pk)
        serializer = SubsidiarySerializer(subsidiary_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        subsidiary_id = self.get_object(pk)
        subsidiary_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SubsidiaryAPIListView(APIView):
    def get(self, request, format=None):
        subsidiary = Subsidiary.objects.all()
        serializer = SubsidiarySerializer(subsidiary, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SubsidiarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubsidiaryOrganizationAPIListView(APIView):
    def get(self, request, organization, format=None):
        subsidiary = Subsidiary.objects.filter(organization=organization)
        serializer = SubsidiarySerializer(subsidiary, many=True)
        return Response(serializer.data)


class CorrelativeAPIView(APIView):
    def get_object(self, pk):
        try:
            return Correlative.objects.get(pk=pk)
        except Correlative.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        correlative_id = self.get_object(pk)
        serializer = CorrelativeSerializer(correlative_id)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        correlative_id = self.get_object(pk)
        serializer = CorrelativeSerializer(correlative_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        correlative_id = self.get_object(pk)
        correlative_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CorrelativeAPIListView(APIView):
    def get(self, request, format=None):
        correlative = Correlative.objects.all()
        serializer = CorrelativeSerializer(correlative, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CorrelativeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
