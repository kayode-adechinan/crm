from rest_framework import serializers
from customer import models


class CustomerSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='customer:customer-detail',
        lookup_field='pk'
    )
    class Meta:
        model = models.Customer
        fields = ('pk','first_name', 'last_name', 'email', 'phone','address','description', 'url')