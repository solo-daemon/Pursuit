from rest_framework import serializers
from pursuit_app.models import Season

class SeasonSerializer (serializers.ModelSerializer) :

    class Meta :
        models = Season
        fields = '__all__'