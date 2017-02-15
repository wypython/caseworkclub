from django.contrib import admin

from .models import Member, Caseworker, Person

from .models import Workplace, Employer, Job, JobType, Association
from .models import Case,CaseworkType,CaseNote,NoteType
from .models import CaseAdmin,CaseTypeAdmin

from .models import PersonAdmin,WorkplaceAdmin

from .models import Task
from .models import User

admin.site.register(Task)

admin.site.register(Member)
admin.site.register(Caseworker)
admin.site.register(Person,PersonAdmin)
admin.site.register(Association)

admin.site.register(Workplace,WorkplaceAdmin)

admin.site.register(Employer)
admin.site.register(Job)
admin.site.register(JobType)

admin.site.register(CaseNote)
admin.site.register(Case,CaseTypeAdmin)
admin.site.register(NoteType)
admin.site.register(CaseworkType,CaseTypeAdmin)

admin.site.register(User)
