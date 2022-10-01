from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from pursuit_app.models import Season
from pursuit_app.serializers import SeasonSerializer

class SeasonViewSet(viewsets.ModelViewSet) :
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [SessionAuthentication ,]

