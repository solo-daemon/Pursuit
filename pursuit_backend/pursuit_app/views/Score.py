# also the grader serializer

from rest_framework import viewsets
from pursuit_app.serializers import ScoreSerializer
from pursuit_app.models import Scores
# wish to use grader viewset
class ScoreViewSet(viewsets.ModelViewSet) :

    seralizer_class = ScoreSerializer
    queryset  =  Scores.objects.all()