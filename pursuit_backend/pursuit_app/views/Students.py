from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from pursuit_app.serializers.Student import StudentSerializer
from pursuit_app.models.Student import Student
from rest_framework.decorators import action
from rest_framework.response import Response

class StudentViewSet(viewsets.ModelViewSet) :
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    @action(
        methods=['GET' ,] ,
        detail = False ,
        url_name = 'season-wise' ,
        url_path = r'season_wise/(?P<season_id>[0-9]+)/' ,
    )
    def Dashboard(self,request,**kwargs) : 
        data = Student.objects.all()
        data_serialized = StudentSerializer(data,many=True)
        return Response(data_serialized.data)

       

        
