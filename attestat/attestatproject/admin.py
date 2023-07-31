from django.contrib import admin
from .models import Question,Answer,Departament,Result,Atchet
from import_export.admin import ImportExportModelAdmin

from django.contrib.auth.models import User, Group
# Register your models here.

class RegisterQuestion(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['questions','id_departament','category']
    

class RegisterAnswer(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['answers','quest','ball']
   

class RegisterDepartament(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['departaments','numberDep','ID_User_Dep']

class RegisterResult(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['departament','users','questions','category','select_answers','good_answers','result_balls']

class RegisterAtchet(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['departament','users','result_balls','res','dt']


admin.site.register(Question,RegisterQuestion)
admin.site.register(Answer,RegisterAnswer)
admin.site.register(Departament,RegisterDepartament)
admin.site.register(Result,RegisterResult)
admin.site.register(Atchet,RegisterAtchet)

