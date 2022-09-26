from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from pursuit_app.models import Round
from pursuit_app.serializers import RoundSerializer

class RoundViewSet(viewsets.ModelViewSet) :
    queryset = Round.objects.all()
    serializer_class = RoundSerializer
    permission_classes = [IsAuthenticated ,]
    authentication_classes = [SessionAuthentication ,]

    
