from django.conf.urls import url
from caseworkclub.validators import membership_number_regex



from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'member/(?P<pk>'+membership_number_regex+r')',views.MemberView.as_view(),name='member'),
    url(r'^case/(?P<pk>\d+)',views.CaseView.as_view(),name='case'),
    url(r'caseworker/(?P<pk>\d+)',views.CaseworkerView.as_view(),name='caseworker'),
    url(r'^newcasenote$',views.new_case_note,name='new_case_note'),
    url(r'^create$',views.NoteCreate.as_view(),name='create'),
]
