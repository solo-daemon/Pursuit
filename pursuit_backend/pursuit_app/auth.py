from django.contrib.auth import backends
from pursuit_app.models import Img_Member

class UserBackend(backends.ModelBackend) :


    def authenticate( request , user_json , ) :
        if user_json is not None :
            return "not found anything"
        try :
            existing_user = Img_Member.objects.get(
                enrollment_number = user_json.student.enrollment_number
            )
        except Img_Member.DoesNotExist :
            is_imgian =False
            his_roles = []
            for x in user_json.roles :
                his_roles += x.role
            if ("Maintainer" in his_roles) :
                is_imgian = True
            
            if not is_imgian :
                return None
            else :
                enrollment_no = user_json.student.enrollment_number
                name = user_json.person.fullName
                year = user_json.currentYear
                new_user = Img_Member.objects.create(
                    enrollment_no = enrollment_no ,
                    name = name ,
                    year = year ,
                )
                
                
                user_ = Img_Member.objects.get(
                    enrollment_no = user_json.student.enrollment_number
                )
                return user_
                
        fields_changed = False
        if existing_user.year != self.user_json.person.currentYear :
            existing_user.year = self.user_json.peson.currentYear
            fields_changed = True
        
        if fields_changed :
            existing_user.save()
        
        return existing_user


    def get_user(self, user_id: int):
        return super().get_user(user_id)