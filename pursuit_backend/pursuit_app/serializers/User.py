from rest_framework import serializers
from pursuit_app.models import Img_Member

class UserSerializer(serializers.ModelSerializer) :

    class Meta :
        model = Img_Member
        fields = '__all__'