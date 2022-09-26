from django.db import models
from pursuit_app.models.Section import Section
from pursuit_app.models.Interview import Interview

class Interview_Marks ( models.Model ) :
    section = models.ForeignKey( Section , on_delete=models.CASCADE )
    interview = models.ForeignKey( Interview , on_delete=models.CASCADE ,related_name='score', null=True ,)
    interview_score = models.PositiveIntegerField( 'interview score' )
