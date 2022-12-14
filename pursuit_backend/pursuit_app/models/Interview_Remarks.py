from django.db import models
from pursuit_app.models.Interview import Interview
from pursuit_app.models.Section import Section

class Interview_Remarks( models.Model ) :
         
    remarks = models.TextField( 'remarks' , )
    interview = models.ForeignKey( Interview , on_delete = models.CASCADE , related_name='remarks' , null=True ,)
    sections = models.ForeignKey( Section , on_delete = models.CASCADE , )
