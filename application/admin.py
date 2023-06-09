from django.contrib import admin
from .models import *

admin.site.register(Testimonial)
admin.site.register(Setting)
admin.site.register(Contact)

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(StudyCategory)

admin.site.register(Lecture)

admin.site.register(Course)