from django.contrib import admin

# Register your models here.
from myadmin.models import AdminLoginModel ,StateModel

class Adminadminloginmodel(admin.ModelAdmin):
    list_display = ['username','password']
admin.site.register(AdminLoginModel)
admin.site.register(StateModel)


