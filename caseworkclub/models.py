from django.db import models
from django.utils import timezone

import caseworkclub.validators

# Create your models here.



class Workplace(models.Model):
    name = models.CharField(max_length=30)
    employer = models.ForeignKey('Employer')

class Person(models.Model): #Base for all the people classes



    surname = models.CharField(max_length=20)
    first_names = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=11,validators=[caseworkclub.validators.phone_validator],blank=True)
    mobile = models.CharField(max_length=11,validators=[caseworkclub.validators.phone_validator],blank=True)


    #class Meta:
    #    abstract = True


class HRContact(Person):
    employer = models.ForeignKey('Employer')

    def __str__(self):
        return("{} {}:{} HR".format(self.first_names,self.surname,self.employer))

class Manager(Person):
    workplace = models.ForeignKey('Workplace')

class Caseworker(Person):
    association = models.ForeignKey('Association')

    def __str__(self):
        return("{} {}, caseworker for {}.".format(self.first_names,self.surname,self.association))

class Member(Person):

    def __str__(self):
        return("{}: {}, {}".format(self.number,self.surname,self.first_names))

    membership_number = models.CharField(max_length=6,primary_key=True,validators=[caseworkclub.validators.membership_number_validator])
    association = models.ForeignKey('Association')

class Case(models.Model):
    def __str__(self):
        return("{} {}, {}, {}".format(self.member.first_names,self.member.surname,self.workplace,self.caseworktype))
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    caseworktype = models.CharField(max_length = 20)
    opened = models.DateField()
    closed = models.DateField(blank=True,null=True)
    workplace = models.ForeignKey('Workplace',on_delete=models.CASCADE)
    caseworker = models.ForeignKey('Caseworker')

class Association(models.Model):
    def __str__(self):
        return("{} association.".format(self.name))
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

    class Meta:
        abstract=True

class EmailNote(CaseNote):

    contact = models.ForeignKey(Person)

    def __str__(self):
        return("Email Contact with {} at {}".format(self.contact,self.timestamp))

class PhoneNote(CaseNote):

    def __str__(self):
        return("Phone Conversation with {} at ".format(self.contact,self.timestamp))

    contact = models.ForeignKey(Person)

class MeetingNote(CaseNote):
    def __str__(self):
        return("Outcome of meeting at {}".format(self.timestamp))

