from django.conf.urls import url
from caseworkclub.validators import membership_number_regex



from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'(?P<membership_number>'+membership_number_regex+r')',views.caseview,name='caseview'),
]
