from django.contrib import admin

# Register your models here.
from admissions.models import Student,teacher

class stu(admin.ModelAdmin):
    list_display=['name','studentclass','rollno','address']
admin.site.register(Student,stu)


class teacheradm(admin.ModelAdmin):
    list_display=['name','exp','subject','contact']

admin.site.register(teacher,teacheradm)
