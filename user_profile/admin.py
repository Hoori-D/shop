from django.contrib import admin

from user_profile.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'image', 'gender']
    list_display_links = ['user']

    readonly_fields = ['user', 'gender']

    search_fields = ['user']

    ordering = ['user']
    sortable_by = ['user', 'gender']