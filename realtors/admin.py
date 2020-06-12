from django.contrib import admin
from .models import Realtor
# Register your models here.

class RealtorAdmin(admin.ModelAdmin):

	list_display = ('name', 'email')

	list_display_links = ( 'name',)
	search_fields = ('name',)
	list_per_page = 25

admin.site.register(Realtor, RealtorAdmin)