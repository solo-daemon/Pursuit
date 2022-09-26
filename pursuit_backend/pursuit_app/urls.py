from rest_framework import routers
from pursuit_app.views import *
# app_name = 'pursuit'

router=routers.DefaultRouter()
router.register(r'user',UserViewSet)
router.register(r'student',StudentViewSet)
router.register(r'question',QuestionViewSet)

app_name = 'pursuit_app'
urlpatterns = router.urls

