from rest_framework import generics
from customer import models
from customer import serializers

class CustomerList(generics.ListCreateAPIView):
    serializer_class = serializers.CustomerSerializer
    queryset = models.Customer.objects.all()

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CustomerSerializer
    queryset = models.Customer.objects.all()    