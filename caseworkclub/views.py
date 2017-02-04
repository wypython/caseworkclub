from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from caseworkclub.models import Case,Member
from django.template import loader
from django.views import generic
from .models import Caseworker
from .forms import CaseNoteForm

def index(request):
    return HttpResponse("Sup, this is the caseworkclub index")

#def caseview(request,id):

#    return HttpResponse("This will be the view that we use, with all the notes from case ID {}. The member is {}".format(id,Case.objects.get(id=id).member.full_name()))

class CaseView(generic.DetailView):
    model = Case


def member(request,membership_number):
    #print(membership_number)
    member = Member.objects.get(membership_number=membership_number)
    cases_of_member = Case.objects.filter(member=Member.objects.get(membership_number=membership_number))
    template = loader.get_template('caseworkclub/index.html')
    context = {
        'cases_of_member' : cases_of_member,
        'name' : member,
    }

    return HttpResponse(template.render(context,request))

class CaseworkerView(generic.DetailView):
    model = Caseworker
    #template_name = 'caseworkclub/caseworker.html'

def new_case_note(request):
    if request.method == "POST":
        form = CaseNoteForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('case',pk=post.case.id)



    else:

        form = CaseNoteForm()
    return render(request, 'caseworkclub/casenoteform.html',{'form':form})
