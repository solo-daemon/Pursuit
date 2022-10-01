from crypt import methods
import requests 
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import login, logout
from pursuit_app.serializers import UserSerializer
from pursuit_app.models import Img_Member
from pursuit_app.auth import UserBackend
# from pesticide_app.auth import CsrfExemptSessionAuthentication
import environ
import os

env = environ.Env(
    # set casting, default value
    MAIL_ENABLED=(bool, False),
    SMTP_LOGIN=(str, 'DEFAULT')
)

# Set the project base directory
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


class UserViewSet(viewsets.ModelViewSet) :
    serializer_class = UserSerializer
    queryset = Img_Member.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication ,]

    @action(
        methods=['POST' , 'GET' ,] ,
        detail = False ,
        url_name = 'onlogin' ,
        url_path = 'onlogin' ,
        permission_classes = [AllowAny] ,
    )
    def on_login (self , request) :
        client_id = env('CLIENT_ID')
        client_secret = env('CLIENT_SECRET')
        redirect_uri = env('REDIRECT_URI')
        desired_state = env('DESIRED_STATUS')

        try :
            authorization_code = self.request.GET.get('code')
        except KeyError:
            return Response(
                {'message': 'No access token was provided in the request.'} ,
                status=status.HTTP_400_BAD_REQUEST ,
            )

        recieved_state = self.request.GET.get('state')
        if(recieved_state != desired_state) :
            return Response(
                data='Internal Server Error. Try Again later.',
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        url = 'https://channeli.in/open_auth/token/'
        data = {
            'client_id': client_id ,
            'client_secret': client_secret ,
            'grant_type': 'authorization_code' ,
            'redirect_uri': redirect_uri ,
            'code': authorization_code ,
        }
        # making post request to get token
        token_data = requests.post(url=url, data=data).json()        
        if 'error' in token_data.keys():
            return Response(
                data=token_data['error'] + str(token_data),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        # retrieving data from token
        access_token = token_data['access_token']
        refresh_token = token_data['refresh_token']

        headers = {
            'Authorization': 'Bearer ' + access_token
        }

        # making request for user data
        user_data = requests.get(
            url='https://channeli.in/open_auth/get_user_data/', headers=headers).json()
        # return Response (
        #     data = user_data , 
        #     status = status.HTTP_200_OK
        # )
        # try :
        #     existing_user = Img_Member.objects.get(
        #         enrollment_number = user_data.student.enrollment_number
        #     )
        # except Img_Member.DoesNotExists :
        #     is_imgian =False
        #     his_roles = []
        #     for x in user_data.roles :
        #         his_roles += x.role
        #     if ("Maintainer" in his_roles) :
        #         is_imgian = True
            
        #     if not is_imgian :
        #         return Response (
        #               data =  "sorry kid better be an imgian in next life" ,
        #               status = status.HTTP_404_BAD_REQUEST ,
        #         )
        #     else :
        #         enrollment_no = user_data.student.enrollment_number
        #         name = user_data.person.fullName
        #         year = user_data.currentYear
        #         new_user = Img_Member(
        #             enrollment_no = enrollment_no ,
        #             name = name ,
        #             year = year ,
        #         )
        #         new_user.save()
        #         login(request = request , user = new_user)
        #         return Response (
        #             data ={
        #                 "message" : "logged in successfully" ,
        #                 "enrollemnt_no" : enrollment_no ,
        #             } ,
        #             status = status.HTTP_202_ACCEPTED ,
        #         )

        user_ = UserBackend.authenticate(request=request , user_json = user_data )
        login(request , user=user_ , backend='pursuit_app.auth.UserBackend')
        
        # fields_changed = False
        # if existing_user.year != user_data.person.currentYear :
        #     existing_user.year = user_data.peson.currentYear
        #     fields_changed = True
        
        # if fields_changed :
        #     existing_user.save()

        # login(request = request , user = existing_user)
        # return Response (
        #     data = {
        #         "message" : "logged in successfully" ,
        #         "enrollment_no" : existing_user.enrollment_no 
        #     } ,
        #     status = status.HTTP_202_ACCEPTED 
        # )
        if user_ is not None :
            return Response (
                {
                    "message" : "Logged in Successfully" ,
                    "enrollment_number" : user_.enrollment_number ,
                } ,
                status = status.HTTP_202_ACCEPTED ,
            )
        else :
            return Response (
                {
                    "message" : "better be a imgian in next life" ,
                } ,
                status = status.HTTP_404_BAD_REQUEST ,
            )
    @action (
            methods = ['POST'] ,
            detail = False ,
            url_name = 'onlogout' ,
            url_path = 'onlogout' ,
    )

    def on_logout(self ,request) :
        logout(request)
        return Response (
            {
                "message" : "logged out successfully" ,
            } ,
            status = status.HTTP_200_OK
        )
            


