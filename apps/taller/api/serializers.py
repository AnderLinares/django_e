from rest_framework.serializers import ModelSerializer

from apps.taller.models import (
    Labour, TypeCheckList, ServiceCheckList, TypeTransport,
    SolicitudeCheckList
)


class LabourSerializer(ModelSerializer):
    class Meta:
        model = Labour
        fields = ["id", "name", "cost_price", "sale_price"]


class ServiceCheckListSerializer(ModelSerializer):
    class Meta:
        model = ServiceCheckList
        fields = ['id', 'name']


class TypeTransportSerializer(ModelSerializer):
    class Meta:
        model = TypeTransport
        fields = ['id', 'name']


class ServiceSolicitudeCheckListSerializer(ModelSerializer):
    class Meta:
        model = SolicitudeCheckList
        fields = ['id', 'name']


class TypeCheckListSerializer(ModelSerializer):
    service_checklist = ServiceCheckListSerializer()
    type_transport = TypeTransportSerializer()
    solicitude_checklist = ServiceSolicitudeCheckListSerializer()

    class Meta:
        model = TypeCheckList
        fields = ['id', 'service_checklist', 'type_transport', 'solicitude_checklist']
