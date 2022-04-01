from rest_framework import serializers, viewsets

from programs import models


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Program
        fields = ("id", "name", "currency", "return_percentage", "bank_id")
        extra_kwargs = {'bank_id': {'required': True}}


class ProgramViewSet(viewsets.ModelViewSet,):
    queryset = models.Program.objects.all()
    serializer_class = ProgramSerializer
