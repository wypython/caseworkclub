from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.views import generic
from .forms import CaseNoteForm, NewCaseForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
import caseworkclub.models as models

@login_required
def index(request):
    return redirect('cases',slug=request.user.username)

@method_decorator(login_required,name='dispatch')
class NoteCreate(generic.edit.CreateView):
    model = models.CaseNote
    fields = ['case','text','contact','notetype','timestamp']


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


@method_decorator(login_required,name='dispatch')
class UserCasesView(generic.DetailView):
    model = models.User
    template_name = 'caseworkclub/caseworker_detail.html'
    slug_field = 'username'
    context_object_name = 'user_to_view'

@method_decorator(login_required,name='dispatch')
class Tasks(generic.DetailView):
    model = models.User
    template_name = 'caseworkclub/tasks_detail.html'
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
def NewCase(request):
    if request.method == "POST":
        form = NewCaseForm(request.POST)
        if form.is_valid():
            newcase = form.save(commit=False)
            newcase.association = request.user.association#Use the logged in user's association without asking, don't really want a user to be able to make cases for another association.
            newcase.save()
            form.save_m2m()#need this due to commit=False)
            return redirect('cases',slug=request.user.username)

    else:
        form = NewCaseForm()#Only allow caseworkers from the logged in user's association
        form.fields["caseworker"].queryset=models.User.objects.filter(association=request.user.association)

    return render(request,'caseworkclub/newcaseform.html',{'form':form})
