from rest_framework import serializers
from .models import locations


class locationsSerializer(serializers.Serializer):
    Date=serializers.CharField(max_length=15) 
    RentedBike=serializers.FloatField(allow_null=True)
    Hour=serializers.IntegerField(default=0)
    Temperature=serializers.FloatField(default=0.0)
    Humidity=serializers.IntegerField(default=0)
    Wind=serializers.FloatField(default=0.0)
    Visibility=serializers.IntegerField(default=0)
    DewPointTemperature=serializers.FloatField(default=0.0)
    SolarRadiation=serializers.FloatField(default=0.0)
    Rainfall=serializers.FloatField(default=0.0)
    Snowfall=serializers.FloatField(default=0.0)
    Season=serializers.CharField(max_length=15)
    Holiday=serializers.CharField(max_length=15) 

    def create(self, validated_data):
        return locations.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.Date = validated_data.get('Date' , instance.Date)
        instance.RentedBike = validated_data.get('Rented Bike Count' , instance.RentedBike )
        instance.Hour = validated_data.get('Hour' , instance.Hour )
        instance.Temperature = validated_data.get('Temperature' , instance.Temperature )
        instance.Humidity = validated_data.get('Humidity' , instance.Humidity )
        instance.Wind = validated_data.get('Windspeed' , instance.Wind )
        instance.Visibility = validated_data.get('Visibility' , instance.Visibility )
        instance.DewPointTemperature = validated_data.get('DewPointTemperature' , instance.DewPointTemperature )
        instance.SolarRadiation = validated_data.get('SolarRadiation' , instance.SolarRadiation )
        instance.Rainfall = validated_data.get('Rainfall' , instance.Rainfall )
        instance.Snowfall = validated_data.get('Snowfall' , instance.Snowfall )
        instance.Season = validated_data.get('Seasons' , instance.Season )
        instance.Holiday = validated_data.get('Holiday' , instance.Holiday )
        instance.save()
        return instance