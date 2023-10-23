from django.contrib import admin
from .models import CustomUser, LifeSituation, Process, Service


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


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_type', 'regulating_act', 'lifesituation', 'user')
    search_fields = ('name', 'service_type', 'regulating_act', 'user__username')
    list_filter = ('service_type', 'lifesituation', 'user')


class ProcessAdmin(admin.ModelAdmin):
    list_display = ('name', 'service', 'status', 'client', 'responsible_authority', 'department')
    search_fields = ('name', 'service__name', 'client', 'responsible_authority', 'department')
    list_filter = ('status', 'client', 'digital_format')
    fieldsets = (
        (None, {'fields': ('name', 'service', 'status', 'client', 'identifier')}),
        ('Responsibility', {'fields': ('responsible_authority', 'department')}),
        ('Digital Format', {'fields': ('digital_format', 'digital_format_link')}),
        ('Data', {'fields': ('client_value', 'input_data', 'output_data', 'related_processes')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(LifeSituation, LifeSituationAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Process, ProcessAdmin)
