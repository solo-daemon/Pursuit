from django.db import models
from pursuit_app.models.Interview import Interview
from pursuit_app.models.Interview_Section import Interview_Section

class Interview_Remarks( models.Model ) :
         
    remarks = models.TextField( 'remarks' , )
    interview = models.ForeignKey( Interview , on_delete = models.CASCADE , related_name='remarks' , null=True ,)
    section = models.ForeignKey(Interview_Section , on_delete = models.CASCADE , related_name='remarks' , null= True ,)

    def __str__(self):
        return str(self.id)