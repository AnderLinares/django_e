from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.taller.models import Labour, TypeCheckList, ServiceCheckList, TypeTransport
from .serializers import (
    LabourSerializer, TypeCheckListSerializer,
    ServiceCheckListSerializer,
    TypeTransportSerializer)


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


class TypeCheckListAPIView(APIView):
    def get_object(self, pk):
        try:
            return TypeCheckList.objects.get(pk=pk)
        except TypeCheckList.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        typechecklist_id = self.get_object(pk)
        serializer = TypeCheckListSerializer(typechecklist_id)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        typechecklist_id = self.get_object(pk)
        serializer = TypeCheckListSerializer(typechecklist_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        typechecklist_id = self.get_object(pk)
        typechecklist_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TypeCheckListAPIListView(APIView):
    def get(self, request, format=None):
        typechecklist = TypeCheckList.objects.all()
        serializer = TypeCheckListSerializer(typechecklist, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TypeCheckListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# service-solicitude
class TypeCheckListServiceAPIListView(APIView):
    def get(self, request, service, typetransport, format=None):
        """
        :param service: service id
        :return: checklist - for - service
        """
        typechecklist = TypeCheckList.objects.filter(
            service_checklist=service, type_transport=typetransport)
        serializer = TypeCheckListSerializer(typechecklist, many=True)
        return Response(serializer.data)


# service
class ServiceCheckListAPIView(APIView):
    def get_object(self, pk):
        try:
            return ServiceCheckList.objects.get(pk=pk)
        except ServiceCheckList.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        service_checklist_id = self.get_object(pk)
        serializer = ServiceCheckListSerializer(service_checklist_id)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        service_checklist_id = self.get_object(pk)
        serializer = ServiceCheckListSerializer(service_checklist_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        service_checklist_id = self.get_object(pk)
        service_checklist_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ServiceCheckListAPIListView(APIView):
    def get(self, request, format=None):
        service_checklist = ServiceCheckList.objects.all()
        serializer = ServiceCheckListSerializer(service_checklist, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ServiceCheckListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# typevehicule
class TypeTransportAPIView(APIView):
    def get_object(self, pk):
        try:
            return TypeTransport.objects.get(pk=pk)
        except TypeTransport.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        type_transport_id = self.get_object(pk)
        serializer = TypeTransportSerializer(type_transport_id)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        type_transport_id = self.get_object(pk)
        serializer = TypeTransportSerializer(type_transport_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        type_transport_id = self.get_object(pk)
        type_transport_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TypeTransportAPIListView(APIView):
    def get(self, request, format=None):
        type_transport = TypeTransport.objects.all()
        serializer = TypeTransportSerializer(type_transport, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TypeTransportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
