from rest_framework import serializers
from author_crud.models.review import Review

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'rating', 'description', 'book')

class ReviewBookSerializer(serializers.ModelSerializer):
    book = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = ('id', 'rating', 'description', 'book')

class ChangeReviewRatingSerializer(serializers.Serializer):
    rating = serializers.IntegerField()

    def validate(self, data):
        if data["rating"] > 10 or data["rating"] < 0:
            raise serializers.ValidationError({
                "rating": "Rating can't be more than 10 and less than 0"
            })
        return data