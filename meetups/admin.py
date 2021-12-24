from django.contrib import admin

# Register your models here.
from .models import Meetup

class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Meetup, MeetupAdmin)