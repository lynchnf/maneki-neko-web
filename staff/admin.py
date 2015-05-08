from django.contrib import admin
from staff.models import Department, Position

class PositionInline(admin.TabularInline):
    model = Position
    extra = 1
    
class DepartmentAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'chair']
    inlines = [PositionInline]
    list_display = ('name', 'email')
    ordering = ['name']
    
admin.site.register(Department, DepartmentAdmin)