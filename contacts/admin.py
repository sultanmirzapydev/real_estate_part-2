from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):

	list_display = ('id', 'name', 'listing', 'email', )
	list_display_links = ('id', 'name', 'email')
	search_fields = ('name', 'email', 'listing')
	list_per_page = 25


admin.site.register(Contact, ContactAdmin)
