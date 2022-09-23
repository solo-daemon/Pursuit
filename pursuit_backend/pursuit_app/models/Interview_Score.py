from django.db import models
from . Section import Section
from . Interview import Interview

class Interview_Marks ( models.Model ) :
    section = models.ForeignKey( Section , on_delete=models.CASCADE )
    interview = models.ForeignKey( Interview , on_delete=models.CASCADE ,realted_name='score', null=True ,)
    interview_score = models.PositiveIntegerField( 'interview score' )
