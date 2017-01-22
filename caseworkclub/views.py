from django.shortcuts import render
from django.http import HttpResponse
from caseworkclub.models import Case

def index(request):
    return HttpResponse("Sup, this is the caseworkclub index")

def caseview(request,id):

    return HttpResponse("This will be the view that we use, with all the notes from case {}. The member is {}".format(id,Case.objects.get(id=id).member.surname))
