from django.contrib import admin
from .models import Contact, Valuation

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'contact_date', 'agent_name')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'listing', 'email', 'agent_name')
    list_per_page = 25
    
class ValuationAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'name', 'phone', 'email', 'request_date')
    list_display_links = ('id', 'address')
    search_fields = ('name', 'address', 'email', 'request_date')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)
admin.site.register(Valuation, ValuationAdmin)

# Register your models here.
