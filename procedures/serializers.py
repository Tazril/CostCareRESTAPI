from rest_framework import serializers
from .models import Hospital, Procedure

class ProcedureSerializer(serializers.ModelSerializer):
    hospital_name = serializers.StringRelatedField(source='hospital.name')
    lat = serializers.StringRelatedField(source='hospital.lat')
    lon = serializers.StringRelatedField(source='hospital.lon')

    class Meta:
        model = Procedure
        fields = ('id', 'name', 'charge', 'hospital', 
                  'last_updated', 'hospital_name', 'lat', 'lon')


class HospitalSerializer(serializers.ModelSerializer):
    procedures = serializers.StringRelatedField(many=True, read_only=True)
    # location = LatLngSerializer()

    class Meta:
        model = Hospital
        fields = ('id', 'name', 'web_url', 'procedures',
                  'contact_num', 'query_url', 'lat', 'lon')
    

class HospitalListSerializer(serializers.ModelSerializer):
    # location = LatLngSerializer()
    class Meta:
        model = Hospital
        fields = ('id', 'name', 'lat', 'lon')
