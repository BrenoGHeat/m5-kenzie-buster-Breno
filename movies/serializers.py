from rest_framework import serializers
from .models import RatingChoices
from .models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, required=False, default="")
    rating = serializers.ChoiceField(choices=RatingChoices.choices, default=RatingChoices.G)
    synopsis = serializers.CharField(required=False, default="")
    added_by = serializers.SerializerMethodField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def get_added_by(self, obj: Movie):

        return obj.user.email
