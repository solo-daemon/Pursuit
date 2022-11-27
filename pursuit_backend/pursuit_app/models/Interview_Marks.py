from django.db import models
from pursuit_app.models.Section import Section
from pursuit_app.models.Interview import Interview
from pursuit_app.models.Interview_Section import Interview_Section

class Interview_Marks ( models.Model ) :
    section = models.ForeignKey(Interview_Section , on_delete = models.CASCADE , related_name='score' , null= True ,)
    interview = models.ForeignKey( Interview , on_delete=models.CASCADE ,related_name='score', null=True ,)
    interview_score = models.PositiveIntegerField( 'interview score' )

    def __str__(self):
        return str(self.id)