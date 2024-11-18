from django.contrib import admin
from newapp.models import Student
class studentdata(admin.ModelAdmin):
    list_display=['id','first_name','last_name']

admin.site.register(Student,studentdata)


