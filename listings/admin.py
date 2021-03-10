from django.contrib import admin
from . models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'is_published', 'price', 'list_date', 'agent')
    list_display_links = ('id', 'address')
    list_filter = ('agent',)
    list_editable = ('is_published',)
    search_fields = ('address', 'city', 'county', 'postcode')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
