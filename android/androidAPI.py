from tastypie import fields
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import Authorization, DjangoAuthorization
from tastypie.constants import ALL_WITH_RELATIONS, ALL
from tastypie.resources import ModelResource
from ermsapp.models import Interview_Interviewer,Interview,Personal,Messages,Personal_Interview_viewer,Personal_Interview
from django.contrib.auth.models import User
from tastypie.api import Api


class UserResource(ModelResource):
    class Meta:

     queryset = User.objects.all()
     resource_name = 'User'
     authentication = BasicAuthentication()
     authorization = DjangoAuthorization()
#no need to edit above

class User02Resource(ModelResource):
    class Meta:

     queryset = User.objects.all()
     resource_name = 'User02'
     fields =['id']
     filtering = {
         'id': ALL
     }

class InterviewResource(ModelResource):
    class Meta:

     queryset = Interview.objects.all()
     resource_name = 'Interview'
     fields =['Time','Date','Venue','Vacancy']
     filtering = {
         'id': ALL
     }

class Interview_InterviewerResource(ModelResource):

    Interviewer = fields.ForeignKey(User02Resource,'Interviewer', full=True)
    Interview = fields.ForeignKey(InterviewResource,'Interview', full=True)

    class Meta:

     queryset = Interview_Interviewer.objects.all()
     resource_name = 'Interview_Interviewer'
     filtering = {
           'Interview': ALL_WITH_RELATIONS,
           'User02': ALL_WITH_RELATIONS
        }
#no need to edit above

class MessagesResource(ModelResource):
    Send02 = fields.ForeignKey(User02Resource,'Send', full=True)

    class Meta:

     queryset = Messages.objects.all()
     resource_name = 'Messages'
     fields =['Send','MsgCont']
     filtering = {
         'User02': ALL_WITH_RELATIONS
     }
#this is also okay

class PersonalResource(ModelResource):
    class Meta:
     queryset = Personal.objects.all()
     resource_name = 'Personal'
     excludes =["SpecialNotes","DeptPost"]
     authorization = Authorization()
     always_return_data = True
     fields = ['NIC','FullName','DOB','DateRecieved','AddressLine1','AddressLine2','AddressLine3','ContactNum','Email','FacebookProf','LinkedInProf']
     filtering = {
        "NIC":ALL_WITH_RELATIONS,
        "FName":ALL_WITH_RELATIONS
        }
#this is okay for tab03 search

class Personal_InterviewResource(ModelResource):
    Personal = fields.ForeignKey(PersonalResource,'Personal', full=True)
    Interview = fields.ForeignKey(InterviewResource,'Interview', full=True)

    class Meta:

     queryset = Personal_Interview.objects.all()
     resource_name = 'Personal_Interview'
     filtering = {
         'Personal' : ALL_WITH_RELATIONS,
         'Interview' : ALL_WITH_RELATIONS
     }

class Personal_Interview_viewerResource(ModelResource):
    class Meta:

        queryset = Personal_Interview_viewer.objects.all()
        resource_name = 'Personal_Interview_viewer'
        authorization = Authorization()
#this is also okay

android_api = Api(api_name='android')

android_api.register(UserResource())
android_api.register(Interview_InterviewerResource())
android_api.register(InterviewResource())
android_api.register(PersonalResource())
android_api.register(Personal_InterviewResource())
android_api.register(Personal_Interview_viewerResource())
android_api.register(MessagesResource())
android_api.register(User02Resource())
