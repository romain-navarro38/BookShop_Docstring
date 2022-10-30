from django.contrib import admin

from account.models import CustomUser


@admin.register(CustomUser)
class AccountConfig(admin.ModelAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_active', )
    list_editable = ('is_staff', 'is_active', )
    search_fields = ('email', 'username', 'first_name', 'last_name', )
    list_filter = ('is_staff', 'is_active', )
