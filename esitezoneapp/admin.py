from django.contrib import admin
from .models import contact

admin.site.site_header ="Esitezone"
admin.site.site_title ="Esitezone"
admin.site.index_title ="Manage contact by admin"



class contactAdmin(admin.ModelAdmin):
    list_display =('name','phone','email','massage')
    search_fields =('name','phone','email','massage')

# Register your models here.
admin.site.register(contact,contactAdmin)