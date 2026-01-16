from django.contrib import admin

from catalog.models import Plant, Category


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'created_at', 'updated_at', 'popularity']
    list_display_links = ['name']
    list_editable = ['price']

    readonly_fields = ['slug', 'created_at', 'updated_at', 'popularity']

    search_fields = ['name']

    ordering = ['name']
    sortable_by = ['name', 'price']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']

    readonly_fields = ['slug']

    search_fields = ['name']

    ordering = ['name']
    sortable_by = ['name']