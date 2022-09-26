from django.db import models
from pursuit_app.models.Round import Round
from pursuit_app.models.Student import Student

class Interview(models.Model) :

    rounds = models.ForeignKey( Round , on_delete = models.CASCADE , )
    student = models.ForeignKey( Student , on_delete = models.CASCADE , related_name='interviews')
    start_time = models.PositiveIntegerField('start time')
    