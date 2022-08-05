from ast import Add
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,SuperAgent,HOD,BookPlot,AddPlot,Customer,Fundtransfer,Installment,phase


# Register your models here.

# class UserModel(UserAdmin):
#     list_display = ['username', 'user_type']


# class UserModel(UserAdmin):
#     pass


class BlogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
    

admin.site.register(CustomUser)
admin.site.register(SuperAgent)
admin.site.register(HOD)
admin.site.register(BookPlot)
admin.site.register(AddPlot,BlogAdmin)
admin.site.register(Customer)
admin.site.register(Fundtransfer)
admin.site.register(Installment)
admin.site.register(phase)
