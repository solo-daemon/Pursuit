from rest_framework import viewsets
from pursuit_app.models import Interview
from pursuit_app.serializers import InterviewSerializer

class InterviewViewSet(viewsets.ModelViewSet) :
    serializer_class = InterviewSerializer
    queryset = Interview.objects.all()
