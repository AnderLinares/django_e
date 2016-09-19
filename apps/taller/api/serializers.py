from rest_framework.serializers import ModelSerializer
from apps.taller.models import Labour


class LabourSerializer(ModelSerializer):
    class Meta:
        model = Labour
        fields = ["id", "name", "cost_price", "sale_price"]
