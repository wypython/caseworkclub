from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.views import generic
from .forms import CaseNoteForm, NewCaseForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
import caseworkclub.models as models


def index(request):
    return HttpResponse("Sup, this is the caseworkclub index")

@method_decorator(login_required,name='dispatch')
class NoteCreate(generic.edit.CreateView):
    model = models.CaseNote
    fields = ['case','text','contact','notetype','timestamp']


@method_decorator(login_required,name='dispatch')
class NewCase(generic.edit.CreateView):
    model = models.Case
    fields = ['member','workplace','caseworktypes','opened','caseworker']

    def form_valid(self,form):#Don't knwo what this does, really - got it from Stack Overflow
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return HttpResponseRedirect(self.get_success_url())


#    def form_valid(self,form):
 #       form.instance.id = self.request.id
@method_decorator(login_required,name='dispatch')
class CaseView(generic.DetailView):
    model = models.Case
    def get_context_data(self, **kwargs):
        context = super(CaseView, self).get_context_data(**kwargs)  
        context['username'] =  self.request.user.username
        print(self.request.user.username)
        return(context)


@method_decorator(login_required,name='dispatch')
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

@method_decorator(login_required,name='dispatch')
class UserCasesView(generic.DetailView):
    model = models.User
    template_name = 'caseworkclub/caseworker_detail.html'
    slug_field = 'username'
    context_object_name = 'user_to_view'
@method_decorator(login_required,name='dispatch')
class AssociationView(generic.DetailView):
    model = models.Association


@login_required
def new_case_note(request):
    if request.method == "POST":
        form = CaseNoteForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('case',pk=post.case.id)



    else:

        form = CaseNoteForm()
    return render(request, 'caseworkclub/casenoteform.html',{'form':form})


@login_required
def createNewCase(request):
    if request.method == "POST":
        form = NewCaseForm(request.POST)
        if form.is_valid():
            newcase = form.save(commit=False)
            newcase.association = request.user.association
            newcase.save()
            return redirect('cases',slug=request.user.username)

    else:
        form = NewCaseForm()
        form.fields["caseworker"].queryset=models.User.objects.filter(association=request.user.association)

    return render(request,'caseworkclub/newcaseform.html',{'form':form})
