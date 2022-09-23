from django.db import models
from . Season import Season
from . Round import Round

class Student ( models.Model ) :
    
    DEVELOPER = 'D'
    DESIGNER = 'd'
    ROLE = [
        (DEVELOPER,'Developer') ,
        (DESIGNER,'Designer') ,
    ]

    DISQUALIFIED = 'D'
    SELECTED = 'S'
    PENDING = 'P'
    SELECTION_STATUS = [
        (DISQUALIFIED , 'disqualified') ,
        (SELECTED , 'selected') ,
        (PENDING , 'pending' ) ,
    ]

    enrollment_no = models.PositiveIntegerField( 'enrollment no' , primary_key='true' , )
    student_name = models.CharField( 'student name' , max_length=255 , )
    department = models.CharField( 'department' , max_length=5 , )#choices to add
    cg = models.DecimalField( 'cg' , max_digits = 3 , decimal_places=1 , )
    season = models.ForeignKey( Season , on_delete = models.CASCADE , )
    status = models.OneToOneField( Round , on_delete=models.CASCADE , )
    role = models.CharField('role' , max_length = 1 , choices = ROLE , default = DEVELOPER , )
    mobile_number = models.CharField( 'mobile number' , max_length=14)
    email = models.EmailField( max_length=254 )
    selection_status = models.CharField('selection status' , choices = SELECTION_STATUS , default = PENDING , max_length=1)

    def __str__(self) :
        return self.enrollment_no
