from rest_framework import serializers
from author_crud.models.review import Review

class ReviewSerializer(serializers.ModelSerializer):
    #book = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = ('id', 'rating', 'description', 'book')
