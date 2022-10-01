from rest_framework import serializers
from pursuit_app.models import Season

class SeasonSerializer (serializers.ModelSerializer) :

    class Meta :
        model = Season
        fields = '__all__'