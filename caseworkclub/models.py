from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

phone_regex = RegexValidator(regex=r'0[0-9]{10}',message="Phonenumber must be 11 digits long and start with 0")
membership_number_regex = RegexValidator(regex=r'[A-Z]\d{5}',message="NUT Membership Numbers have a capital letter and five digits.")

class Workplace(models.Model):
    name = models.CharField(max_length=30)
    employer = models.ForeignKey('Employer')

class Person(models.Model): #HR, Headteacher etc.

    surname = models.CharField(max_length=20)
    first_names = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=11,validators=[phone_regex],blank=True)
    mobile = models.CharField(max_length=11,validators=[phone_regex],blank=True)


    class Meta:
        abstract = True


class HRContact(Person):
    employer = models.ForeignKey('Employer')

class Manager(Person):
    workplace = models.ForeignKey('Workplace')

class Caseworker(Person):
    association = models.ForeignKey('Association')

    def __str__(self):
        return("{} {}, caseworker for {}.".format(self.first_names,self.surname,self.association))

class Member(Person):

    def __str__(self):
        return("{}: {}, {}".format(self.number,self.surname,self.first_names))

    membership_number = models.CharField(max_length=6,primary_key=True,validators=[membership_number_regex])
    association = models.ForeignKey('Association')

class Case(models.Model):
    def __str__(self):
        return("{}: {}, {}, {}".format(self.member.number,self.member.surname,self.member.first_names,self.caseworktype))
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

class Employer(models.Model): #LA, Academy Trust etc.
    name = models.CharField(max_length = 20)
    facility_time = models.BooleanField("Pays into facility time pot")
