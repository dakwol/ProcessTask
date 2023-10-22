from django.contrib import admin
from .models import CustomUser, LifeSituation


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'patronymic')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'patronymic')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'date_joined')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'patronymic')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )


class LifeSituationAdmin(admin.ModelAdmin):
    list_display = ('name', 'identifier', 'user')
    search_fields = ('name', 'identifier', 'user__username')
    list_filter = ('user',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(LifeSituation, LifeSituationAdmin)
