from django.forms import ModelForm


from caseworkclub.models import CaseNote

class CaseNoteForm(ModelForm):
    class Meta:
        model = CaseNote
        fields = ['timestamp','case','contact','notetype','text']
