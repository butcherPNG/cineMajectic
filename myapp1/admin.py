from django.contrib import admin
from .models import SearchQuery
from myapp1.models import *


# Register your models here.

admin.site.register(User)

@admin.register(SearchQuery)
class SearchQueryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_date_formatted')

    def created_date_formatted(self, obj):
        return obj.created_date.strftime("%d-%m-%Y %H:%M:%S")

    created_date_formatted.short_description = 'Created At'
