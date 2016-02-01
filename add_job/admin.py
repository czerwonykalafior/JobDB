from django.contrib import admin
from add_job.models import Job, Branza, Tag


class JobAdmin(admin.ModelAdmin):
    list_display = ('stanowisko', 'opis')
    search_fields = ('stanowisko',)
    list_filter = ('tags',)
    filter_horizontal = ('branze',)


admin.site.register(Job, JobAdmin)
admin.site.register(Branza)
admin.site.register(Tag)

# Register your models here.
