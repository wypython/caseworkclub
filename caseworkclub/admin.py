from django.contrib import admin

from .models import Member, Caseworker, Manager, HRContact
from .models import Workplace, Employer, Association
from .models import Case



admin.site.register(Member)
admin.site.register(Case)
admin.site.register(Caseworker)
admin.site.register(Association)


admin.site.register(Workplace)
admin.site.register(Manager)
admin.site.register(HRContact)


admin.site.register(Employer)

