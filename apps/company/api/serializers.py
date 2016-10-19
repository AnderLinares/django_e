from rest_framework.serializers import ModelSerializer

from apps.company.models import (
   Organization, Subsidiary, Correlative
)


class OrganizationSerializer(ModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"


class SubsidiarySerializer(ModelSerializer):
    organization = OrganizationSerializer()

    class Meta:
        model = Subsidiary
        fields = "__all__"


class CorrelativeSerializer(ModelSerializer):
    organization = OrganizationSerializer()
    subsidiary = SubsidiarySerializer()

    class Meta:
        model = Correlative
        fields = "__all__"
