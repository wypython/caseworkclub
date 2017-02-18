from django.conf.urls import url,include
from caseworkclub.validators import membership_number_regex
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login,logout


from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'member/(?P<pk>'+membership_number_regex+r')',views.MemberView.as_view(),name='member'),
    url(r'^case/(?P<pk>\d+)',views.CaseView.as_view(),name='case'),
    url(r'cases/(?P<slug>\w+)',views.UserCasesView.as_view(),name='cases'),
    url(r'^newcasenote$',views.new_case_note,name='new_case_note'),
    url(r'^create$',views.NoteCreate.as_view(),name='create'),
    url(r'^(?i)association/(?P<pk>\w*)',views.AssociationView.as_view(),name='association'),
    url(r'^login/$',login,name='login'),
    url(r'^logout/$',logout,name='logout'),
    ]

