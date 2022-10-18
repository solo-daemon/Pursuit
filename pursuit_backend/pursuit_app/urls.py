from rest_framework import routers
from pursuit_app.views import *

# app_name = 'pursuit'

router=routers.DefaultRouter()
router.register(r'user',UserViewSet,"user")
router.register(r'student',StudentViewSet,"student")
router.register(r'question',QuestionViewSet,"question")
router.register(r'season',SeasonViewSet,"season")
router.register(r'round',RoundViewSet,"round")
router.register(r'section',SectionViewSet,"section")
router.register(r'question',QuestionViewSet,"question")
router.register(r'interview',InterviewViewSet,"interview")
router.register(r'interview_remarks',Interview_RemarksViewSet,"interview-remarks")
router.register(r'interview_marks',Interview_MarksViewSet,"interview-marks")
router.register(r'interview_panel',Interview_PanelViewSet,"interview-panel")
router.register(r'score',ScoreViewSet,"score")

app_name = 'pursuit_app'
urlpatterns = router.urls

