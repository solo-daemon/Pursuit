from rest_framework import viewsets
from rest_framework.decorators import action
from pursuit_app.serializers.Student import StudentSerializer
from pursuit_app.models.Student import Student

class StudentViewSet(viewsets.ModelViewSet) :
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    @action(detail=True, 
    methods=['list'] ,
    url_path='dashboard' ,
    url_name='dashboard' ,)
    def dashboard(self , request) :
        pass