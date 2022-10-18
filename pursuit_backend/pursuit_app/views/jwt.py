from rest_framework_simplejwt.views import TokenObtainPairView
from pursuit_app.serializers import TokenObtainPairWithoutPasswordSerializer


class TokenObtainPairWithoutPasswordView(TokenObtainPairView):
    serializer_class = TokenObtainPairWithoutPasswordSerializer