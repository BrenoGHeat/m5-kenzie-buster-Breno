from rest_framework import serializers
from .models import MovieOrder


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    title = serializers.SerializerMethodField()
    purchased_at = serializers.DateTimeField(read_only=True)
    purchased_by = serializers.SerializerMethodField()

    def get_purchased_by(self, obj: MovieOrder):

        return obj.user.email

    def get_title(self, obj: MovieOrder):

        return obj.movie.title

    def create(self, validated_data):
        return MovieOrder.objects.create(**validated_data)
