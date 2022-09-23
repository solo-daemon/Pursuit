from rest_framework import viewsets
from pursuit_app.serializers import QuestionSerializer
from pursuit_app.models import Question

class QuestionViewSet(viewsets.ModelViewSet) :

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer