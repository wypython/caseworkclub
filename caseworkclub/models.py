from django.db import models
from django.utils import timezone
from django.contrib import admin
import caseworkclub.validators

from django.urls import reverse
# Create your models here.



class Workplace(models.Model):
    name = models.CharField(max_length=30)
    employer = models.ForeignKey('Employer')

    def __str__(self):
        return(self.name)

class Person(models.Model): #Base for all the people classes



    surname = models.CharField(max_length=20)
    first_names = models.CharField(max_length=20)

    def full_name(self):
        return("{} {}".format(self.first_names,self.surname))

    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=11,validators=[caseworkclub.validators.phone_validator],blank=True)
    mobile = models.CharField(max_length=11,validators=[caseworkclub.validators.phone_validator],blank=True)

    workplace = models.ManyToManyField(Workplace,through='Job')
    
    def __str__(self):
        return(self.full_name())

class Job(models.Model):
    title = models.ForeignKey('JobType')
    workplace = models.ForeignKey(Workplace, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

class JobType(models.Model):
    typename = models.CharField(max_length=2)
    def __str__(self):
        return(self.typename)

class Caseworker(Person):
    association = models.ForeignKey('Association')

    def __str__(self):
        return(self.full_name())

    def open_cases(self):
        return(Case.objects.filter(closed=None,caseworker=self))



class Member(Person):

    membership_number = models.CharField(max_length=6,primary_key=True,validators=[caseworkclub.validators.membership_number_validator])
    association = models.ForeignKey('Association')
    
    def cases_of_member(self):
        return(Case.objects.filter(member=self))

    def __str__(self):
        return("{} {}".format(self.full_name(),self.membership_number))
class CaseworkType(models.Model):
    typename = models.CharField(max_length = 20)

    def __str__(self):
        return(self.typename)

    def cases_of_type(self):
        return(Case.objects.filter(caseworktype=self))


class Case(models.Model):
    def __str__(self):
        return("ID={}: {} {}, {}, {}".format(self.id,self.member.first_names,self.member.surname,self.workplace,self.caseworktype))
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    caseworktype = models.ForeignKey(CaseworkType)
    opened = models.DateField()
    closed = models.DateField(blank=True,null=True)
    workplace = models.ForeignKey('Workplace',on_delete=models.CASCADE)
    caseworker = models.ForeignKey('Caseworker')

    def notes(self):
        return(CaseNote.objects.filter(case=self))

class Association(models.Model):
    def __str__(self):
        return(self.name)
    name = models.CharField(max_length = 20)

class Employer(models.Model):
    name = models.CharField(max_length = 20)
    facility_time = models.BooleanField("Pays into facility time pot")

    def __str__(self):
        return(self.name)


class CaseNote(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    case = models.ForeignKey(Case)
    text = models.TextField()
    contact = models.ForeignKey(Person,null=True)
    notetype = models.ForeignKey('NoteType')

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return("{} {} {}".format(self.contact,self.notetype,self.timestamp))
    def get_absolute_url(self):
        return(reverse('case', kwargs ={'pk':self.case.id}))

class NoteType(models.Model):
    name = models.CharField(max_length = 20)
    def __str__(self):
        return(self.name)

class JobInline(admin.TabularInline):
    model = Job
    extra = 1

class PersonAdmin(admin.ModelAdmin):
    inlines = [JobInline]

class WorkplaceAdmin(admin.ModelAdmin):
    inlines = [JobInline]
    exclude = ('Workplace',)
