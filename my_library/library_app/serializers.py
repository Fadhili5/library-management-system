from rest_framework import serializers
from library_app.models import Book
from datetime import datetime
from django.utils import timezone

class BookSerializer(serializers.ModelSerializer):
    
    days_since_created = serializers.SerializerMethodField()
    class Meta:
        model = Book
        # fields = '__all__'
        fields = ['id', 'title', 'author', 'published_date', 'isbn', 'pages', 'created_at', 'updated_at', 'days_since_created']
        read_only_fields = ['created_at', 'updated_at', 'days_since_created']
        
    def get_days_since_created(self, obj):
        if obj.created_at:
            now = timezone.now()
            delta = now - obj.created_at
            return delta.days
        return 0
    
    def validate_isbn(self, value):
        if value and len(value) not in [10, 13]:
            raise serializers.ValidationError("ISBN must be either 10 or 13 characters long.")
        return value
    
    def validate(self, data):
        if data.get('published_date') and data['published_date'] > timezone.now().date():
            raise serializers.ValidationError("Published date cannot be in the future.")
        return data
    
    