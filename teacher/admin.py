from django.contrib import admin
from .models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id','ad_soyad','email','tarix')
    list_display_links = ('ad_soyad',)


# Register your models here.
admin.site.register(Teacher,TeacherAdmin)