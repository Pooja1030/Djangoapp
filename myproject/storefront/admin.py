from django.contrib import admin
from .models import Person, Skill, Location, JobTitle

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'location', 'job_title')
    filter_horizontal = ('skills',)

admin.site.register(Skill)
admin.site.register(Location)
admin.site.register(JobTitle)
