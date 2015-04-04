from django.contrib import admin
from staff.models import ContactUsLog, Department, Position

class PositionInline(admin.TabularInline):
    model = Position
    extra = 1
    
class DepartmentAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'chair']
    inlines = [PositionInline]
    list_display = ('name', 'email')
    ordering = ['name']
    
admin.site.register(Department, DepartmentAdmin)

class ContactUsLogAdmin(admin.ModelAdmin):
    list_display = ['from_email', 'to_department_id', 'to_department', 'to_email', 'subject', 'timestamp', 'sent_successfully']

admin.site.register(ContactUsLog, ContactUsLogAdmin)

class PositionAdmin(admin.ModelAdmin):
    list_display = ['department', 'user', 'title']

admin.site.register(Position, PositionAdmin)