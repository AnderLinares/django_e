from rest_framework.serializers import ModelSerializer

from apps.zone.models import (
    Zone, Country, State
)


class ZoneSerializer(ModelSerializer):
    class Meta:
        model = Zone
        fields = "__all__"


class CountrySerializer(ModelSerializer):
    zone = ZoneSerializer()

    class Meta:
        model = Country
        fields = "__all__"


class StateSerializer(ModelSerializer):
    zone = ZoneSerializer()
    country = CountrySerializer()

    class Meta:
        model = State
        fields = "__all__"
