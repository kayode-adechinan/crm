from rest_framework import serializers

from quote import models

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Quote
        fields = '__all__'