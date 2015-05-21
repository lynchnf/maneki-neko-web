from datetime import datetime
import logging

from django.contrib import admin
from django.db.models import TextField
from django.forms import ModelForm
from django.forms import ValidationError
from djangocms_text_ckeditor.widgets import TextEditorWidget

from news.models import Story


logger = logging.getLogger(__name__)

class StoryForm(ModelForm):
    def clean(self):
        cleaned_data = super(StoryForm, self).clean()
        status = cleaned_data.get("status")
        publish_date = cleaned_data.get("publish_date")
        if status in (2, 3) and not publish_date:
            raise ValidationError("Publish date is required if Status is not Draft.")
        return cleaned_data

    class Meta:
        model = Story

class StoryAdmin(admin.ModelAdmin):
    actions = ['make_draft', 'make_publish', 'make_email', 'make_archive']
    list_display = ('title', 'status', 'publish_date')
    list_filter = ('status', 'publish_date')
    form = StoryForm
    formfield_overrides = {
        TextField: {'widget': TextEditorWidget}                           
    }
    ordering = ['status', '-publish_date', '-id']
    readonly_fields = ("status",)
    search_fields = ['title', 'content']              

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super(StoryAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def make_draft(self, request, queryset):
        for obj in queryset:
            obj.status = 1
            obj.save()
    make_draft.short_description = "Draft selected news stories"
            
    def make_publish(self, request, queryset):
        for obj in queryset:
            obj.status = 2
            if not obj.publish_date:
                obj.publish_date = datetime.today()
            obj.save()
    make_publish.short_description = "Publish selected news stories"
            
    def make_email(self, request, queryset):
        for obj in queryset:
            obj.status = 3
            if not obj.publish_date:
                obj.publish_date = datetime.today()
            obj.save()
    make_email.short_description = "Mass email selected news stories"
            
    def make_archive(self, request, queryset):
        for obj in queryset:
            obj.status = 4
            obj.save()
    make_archive.short_description = "Archive selected news stories"

admin.site.register(Story, StoryAdmin)
