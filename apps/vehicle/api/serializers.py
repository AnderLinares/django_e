from rest_framework.serializers import ModelSerializer

from core.api.serializers import VehicleBrandSerializer, VehicleModelSerializer, VehicleEnrollmentSerializer
from apps.vehicle.models import (
    Vehicle
)


class VehicleSerializer(ModelSerializer):
    brand = VehicleBrandSerializer()
    model = VehicleModelSerializer()
    year_car = VehicleEnrollmentSerializer()

    class Meta:
        model = Vehicle
        fields = "__all__"
