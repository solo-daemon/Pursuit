from rest_framework import serializers
from pursuit_app.models import Interview


class InterviewSerializer(serializers.ModelSerializer) :

    class Meta :
        model = Interview
        fields = '__all__'