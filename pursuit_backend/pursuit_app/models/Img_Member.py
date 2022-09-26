from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

class Img_Member(AbstractBaseUser) :
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
    
    enrollment_no = models.PositiveIntegerField('enrollemnt no' , unique=True)
    name = models.CharField('name' , max_length = 255 , )
    year = models.CharField('year' , max_length = 1 , choices=YEAR , )
    password = models.CharField('password' , max_length= 1 , null=True)
    def __str__(self) :
        return "hello"

    USERNAME_FIELD = 'enrollment_no'
    REQUIRED_FIELDS = []

    # class Meta:
    #     abstract = True 
    #     app_label = 'pursuit_app'