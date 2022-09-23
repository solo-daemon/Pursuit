from django.db import models
from . Student import Student
from . Question import Question
    
class Scores(models.Model) :

    student = models.ForeignKey( Student , on_delete = models.CASCADE , )
    question = models.ForeignKey ( Question , on_delete = models.CASCADE , )
    score = models.PositiveIntegerField( 'score' , )
    remark = models.TextField( 'remark' ,)