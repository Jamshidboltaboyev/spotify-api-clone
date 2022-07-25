from rest_framework import serializers

from .models import Albums


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albums
        fields = "__all__"
