from django.db import models
from . Round import Round
from . Student import Student

class Interview(models.Model) :

    rounds = models.ForeignKey( Round , on_delete = models.CASCADE , )
    student = models.ForeignKey( Student , on_delete = models.CASCADE , related_name='interviews')
    start_time = models.PositiveIntegerField('start time')
    