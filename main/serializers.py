from rest_framework import serializers

from .models import CreateArtist, TestCreate

class CreateArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateArtist
        fields = '__all__'

class TestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCreate
        fields = '__all__'