from dataclasses import field
from rest_framework import serializers
from pursuit_app.models import Student
class StudentSerializer(serializers.ModelSerializer) :


    
    class Meta :
        model = Student
        fields = '__all__'

# class StudentDashboardSerializer(serializers.ModelSerailizer) :

#     class Meta :
#         model = Student
#         field = '__all__'

class StudentDashbaordSerializer(serializers.ModelSerializer) :
    pass
