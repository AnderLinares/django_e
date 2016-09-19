from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from apps.taller.models import Labour
from .serializers import LabourSerializer


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
