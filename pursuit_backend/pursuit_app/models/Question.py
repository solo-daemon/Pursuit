from django.db import models
from . Section import Section
from . Img_Member import Img_Member

class Question( models.Model ) : 

    question = models.TextField('question')
    sections = models.ForeignKey( Section , on_delete = models.CASCADE , )
    maximum_score = models.PositiveIntegerField( 'maximum score' )
    # checker = there can be multiple checker for the same question
    checker = models.ManyToManyField(Img_Member ,)
