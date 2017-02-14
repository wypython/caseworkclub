from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.views import generic
from .forms import CaseNoteForm

import caseworkclub.models as models


def index(request):
    return HttpResponse("Sup, this is the caseworkclub index")

class NoteCreate(generic.edit.CreateView):
    model = models.CaseNote
    fields = ['case','text','contact','notetype','timestamp']

#    def form_valid(self,form):
 #       form.instance.id = self.request.id

class CaseView(generic.DetailView):
    model = models.Case

class MemberView(generic.DetailView):
    model = models.Member

##def member(request,membership_number):
#    member = models.Member.objects.get(membership_number=membership_number)
##    cases_of_member = models.Case.objects.filter(member=models.Member.objects.get(membership_number=membership_number))
#    template = loader.get_template('caseworkclub/index.html')
#    context = {
#
#        'cases_of_member' : cases_of_member,
#        'name' : member,
#    }

    #return HttpResponse(template.render(context,request))

class CaseworkerView(generic.DetailView):
    model = models.Caseworker

class AssociationView(generic.DetailView):
    model = models.Association

def new_case_note(request):
    if request.method == "POST":
        form = CaseNoteForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('case',pk=post.case.id)



    else:

        form = CaseNoteForm()
    return render(request, 'caseworkclub/casenoteform.html',{'form':form})
