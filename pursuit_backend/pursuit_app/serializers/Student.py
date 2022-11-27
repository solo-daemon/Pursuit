from dataclasses import field
from rest_framework import serializers
from pursuit_app.models import Student
class StudentSerializer(serializers.ModelSerializer) :
 
    class Meta :
        model = Student
        fields = '__all__'



