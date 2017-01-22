from django.shortcuts import render
from django.http import HttpResponse
from caseworkclub.models import Case,Member
from django.template import loader

def index(request):
    return HttpResponse("Sup, this is the caseworkclub index")

def caseview(request,id):

    return HttpResponse("This will be the view that we use, with all the notes from case ID {}. The member is {}".format(id,Case.objects.get(id=id).member.surname))

def member(request,membership_number):
    #print(membership_number)
    member = Member.objects.get(membership_number=membership_number)
    print(member.full_name())
    cases_of_member = Case.objects.filter(member=Member.objects.get(membership_number=membership_number))
    template = loader.get_template('caseworkclub/index.html')
    context = {
        'cases_of_member' : cases_of_member,
        'name' : member,
    }

    return HttpResponse(template.render(context,request))

