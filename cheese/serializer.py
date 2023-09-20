from .models import Cheese
from rest_framework import serializers

#Cheese Serializer (to turn our models into JSON strings and then into python dictionaries, and make them ~pretty~)
class CheeseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # the model we wan to serialize
        model = Cheese
        # fields included in that model
        fields = ['id', 'name', 'origin_country', 'type']