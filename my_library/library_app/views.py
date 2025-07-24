import rest_framework
from django.shortcuts import render
from rest_framework import generics
from library_app.serializers import BookSerializer
from library_app.models import Book

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Create your views here.
