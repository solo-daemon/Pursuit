from django.db import models


class Img_Member(models.Model) :
    FIRST = '1'
    SECOND = '2'
    THIRD = '3'
    FOURTH = '4'
    FIFTH = '5'
    YEAR = [
        (FIRST , 'First'),
        (SECOND , 'Second'),
        (THIRD , 'Third'),
        (FOURTH, 'Fourth'),
        (FIFTH , 'Fifth'),
    ]
    
    enrollment_no = models.PositiveIntegerField('enrollemnt no')
    name = models.CharField('name' , max_length = 255 , )
    year = models.CharField('year' , max_length = 1 , choices=YEAR , )
    def __str__(self) :
        return "hello"
