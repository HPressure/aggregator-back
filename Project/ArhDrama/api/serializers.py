from rest_framework import serializers
from ArhDrama.models import Show


class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show
        fields = ('Id', 'Title', 'Description',
                  'Img', 'BuyUrl', 'Date', 'Hour')
