from rest_framework import serializers

from Aplications.client.models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        exclude = ["is_active"]
