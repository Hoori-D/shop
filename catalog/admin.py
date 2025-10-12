from django.contrib import admin

from catalog.models import Plant


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    list_display_links = ['name']
    list_editable = ['price']

    readonly_fields = ['slug']

    search_fields = ['name']

    ordering = ['name']
    sortable_by = ['name', 'price']