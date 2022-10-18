from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from pursuit_app.serializers.Student import StudentSerializer
from pursuit_app.models.Student import Student

class StudentViewSet(viewsets.ModelViewSet) :
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [SessionAuthentication ,]

    # @action(detail=True, 
    # methods=['list'] ,
    # url_path='dashboard' ,
    # url_name='dashboard' ,
    # detail=True,)
    # def dashboard(self , request) :
    #     pass;