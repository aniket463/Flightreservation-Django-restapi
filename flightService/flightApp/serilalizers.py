from rest_framework import serializers
from .models import Flight,Passenger,Reservation
import re

def isFlightNumberValidate(data):
    print(data)
    print('isFlightNumberValidate')


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
        validators = [isFlightNumberValidate]
    
    def validate_flightnumber(self,flightnumber):
        print('validate_flightnumber')
        if(re.match("^[a-zA-Z0-9]*$",flightnumber)==None):
            raise serializers.ValidationError("Invalid flight number")
        return flightnumber

    def validate(self,data):
        print('validate')
        print(data['flightnumber'])
        print(data)
        return data

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'