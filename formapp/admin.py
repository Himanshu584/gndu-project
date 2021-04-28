from django.contrib import admin
from .models import *

# admin customization
admin.site.site_header = "GNDU REGISTRATION FORM" 

# admin model customizations

class CandidatesAdmin(admin.ModelAdmin):
    list_display = ["name", "phone", "email", "catagory", "course"]
    search_fields = ["name", "phone", "email", "catagory", "course"]


# Register your models here.
admin.site.register(Candidates,CandidatesAdmin)
admin.site.register(Courses)
