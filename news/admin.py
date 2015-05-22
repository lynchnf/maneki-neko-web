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
    readonly_fields = ("status", "email_timestamp")
    search_fields = ['title', 'content']              

    def get_actions(self, request):
        actions = super(StoryAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

    def make_draft(self, request, queryset):
        success_count = 0
        skip_count = 0
        for obj in queryset:
            if not obj.email_timestamp:
                obj.status = 1
                obj.save()
                success_count += 1
            else:
                skip_count += 1
        success_msg = "No news stories were unpublished."
        if success_count == 1:
            success_msg = "Successfully unpublished 1 news story."
        elif success_count > 1:
            success_msg = "Successfully unpublished %s news stories." % (success_count)
        self.message_user(request, success_msg)
        if skip_count > 0:
            if skip_count == 1:
                skip_msg = "Skipped 1 news story."
            else:
                skip_msg = "Skipped %s news stories." % (skip_count)
            self.message_user(request, skip_msg)
            
    def make_publish(self, request, queryset):
        success_count = 0
        for obj in queryset:
            obj.status = 2
            if not obj.publish_date:
                obj.publish_date = datetime.today()
            obj.save()
            success_count += 1
        success_msg = "No news stories were published."
        if success_count == 1:
            success_msg = "Successfully published 1 news story."
        elif success_count > 1:
            success_msg = "Successfully published %s news stories." % (success_count)
        self.message_user(request, success_msg)
            
    def make_email(self, request, queryset):
        success_count = 0
        skip_count = 0
        for obj in queryset:
            if not obj.email_timestamp:
                obj.status = 3
                if not obj.publish_date:
                    obj.publish_date = datetime.today()
                if not obj.email_timestamp:
                    obj.email_timestamp = datetime.now()
                obj.save()
                success_count += 1
            else:
                skip_count += 1
        success_msg = "No news stories were emailed."
        if success_count == 1:
            success_msg = "Successfully emailed 1 news story."
        elif success_count > 1:
            success_msg = "Successfully emailed %s news stories." % (success_count)
        self.message_user(request, success_msg)
        if skip_count > 0:
            if skip_count == 1:
                skip_msg = "Skipped 1 news story."
            else:
                skip_msg = "Skipped %s news stories." % (skip_count)
            self.message_user(request, skip_msg)
            
    def make_archive(self, request, queryset):
        success_count = 0
        for obj in queryset:
            obj.status = 4
            obj.save()
            success_count += 1
        success_msg = "No news stories were archived."
        if success_count == 1:
            success_msg = "Successfully archived 1 news story."
        elif success_count > 1:
            success_msg = "Successfully archived %s news stories." % (success_count)
        self.message_user(request, success_msg)

    make_draft.short_description = "Unpublish selected news stories"
    make_publish.short_description = "Publish selected news stories"
    make_email.short_description = "Mass email selected news stories"
    make_archive.short_description = "Archive selected news stories"

admin.site.register(Story, StoryAdmin)
