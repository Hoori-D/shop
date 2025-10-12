from django.contrib import admin

from catalog.models import Plant


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'created_at', 'updated_at']
    list_display_links = ['name']
    list_editable = ['price']

    readonly_fields = ['slug', 'created_at', 'updated_at']

    search_fields = ['name']

    ordering = ['name']
    sortable_by = ['name', 'price']