from django.contrib import admin
from . models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'is_published', 'price', 'list_date', 'agent')
    list_display_links = ('id', 'address')
    list_filter = ('agent', 'sale_agreed', 'sold' ,'city', 'county')
    list_editable = ('is_published',)
    search_fields = ('address', 'city', 'county', 'agent', 'sold', 'city', 'county')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
