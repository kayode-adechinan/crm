from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from quote import models
from quote import serializers

class QuoteList(generics.ListCreateAPIView):
    serializer_class = serializers.QuoteSerializer
    queryset = models.Quote.objects.all()

class QuoteDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.QuoteSerializer
    queryset = models.Quote.objects.all()    