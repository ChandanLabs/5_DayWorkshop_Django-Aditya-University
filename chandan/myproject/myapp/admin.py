from django.contrib import admin
from .models import Info

# Register your models here.

class InfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'age', 'salary', 'created_at')
    list_filter = ('created_at', 'age')
    search_fields = ('name', 'email')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

admin.site.register(Info, InfoAdmin)
