
from unittest.mock import NonCallableMock
from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager , PermissionsMixin


class UserAccountManager(BaseUserManager) :

    def create_user(self,enrollment_no, **other_fields) :
        if not enrollment_no :
            raise ValueError('invalid enrollment number')

        user = self.model(enrollment_no  , **other_fields)
        user.set_unusable_password()
        user.save()

        return user


    def create_superuser(self, enrollment_no , password) :

        user = self.create_user(enrollment_no , password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class Img_Member(AbstractBaseUser , PermissionsMixin) :
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
    is_active = models.BooleanField(default = True ,)
    is_staff = models.BooleanField(default = False ,)
    is_superuser = models.BooleanField(default = False ,)
    password = models.CharField('password' , max_length= 10 , null=True)
    def __str__(self) :
        return "hello"

    objects = UserAccountManager()

    USERNAME_FIELD = 'enrollment_no'
    REQUIRED_FIELDS = ['name' , 'year']

    def __str__(self):
        return str(self.enrollment_no)
    


    