from django.contrib import admin
from .models import Flan, ContactForm

# Register your models here.
@admin.register(Flan)
class FlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'flan_uuid', 'is_private')
    
admin.site.register(ContactForm)
