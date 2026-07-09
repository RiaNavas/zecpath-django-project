from django.contrib import admin
from .models import User, Employer, Candidate, Job, Application


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'role', 'is_active', 'is_verified')
    list_filter = ('role', 'is_active', 'is_verified')


admin.site.register(Employer)
admin.site.register(Candidate)
admin.site.register(Job)
admin.site.register(Application)