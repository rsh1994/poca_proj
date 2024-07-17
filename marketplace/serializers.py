from rest_framework import serializers
from .models import PhotoCard, Sale, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'cash']

class PhotoCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoCard
        fields = ['id', 'name']

class SaleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['id', 'photo_card_id', 'price']

class SaleDetailSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Sale
        fields = ['id', 'price', 'fee', 'total_price']

    def get_total_price(self, obj):
        return obj.price + obj.fee

