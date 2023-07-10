from django.contrib import admin
from .models import Course, Location, Participant

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')
    list_filter = ('location', 'date')
    prepopulated_fields = {'slug': ('title', )}

admin.site.register(Course, CourseAdmin)
admin.site.register(Location)
admin.site.register(Participant)