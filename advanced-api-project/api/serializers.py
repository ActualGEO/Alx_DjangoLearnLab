from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

class AuthorSerializer(serializers.ModelSerializer):
    """The author serializer serialize the author model"""
    class Meta:
        model = Author
        fields = ['name']


class BookSerializer(serializers.ModelSerializer):
    """The book serializer serialize the book model,
       and shows the detailss of the author
    """
    author = AuthorSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = ['title', 'publication_date', 'author']
        
    def validate_publication_date(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError('Publication date shouls be the present date you want to publish')
        return value
