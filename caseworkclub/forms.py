from django.forms import ModelForm


from caseworkclub.models import CaseNote,Case

class CaseNoteForm(ModelForm):
    class Meta:
        model = CaseNote
        fields = ['timestamp','case','contact','notetype','text']

class NewCaseForm(ModelForm):
    class Meta:
        model = Case
        fields = ['member','workplace','caseworktypes','opened','caseworker']
