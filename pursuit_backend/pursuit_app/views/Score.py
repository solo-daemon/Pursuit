# also the grader serializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from pursuit_app.serializers import ScoreSerializer
from pursuit_app.models import Scores
# wish to use grader viewset
class ScoreViewSet(viewsets.ModelViewSet) :

    serializer_class = ScoreSerializer
    queryset  =  Scores.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication ,]
