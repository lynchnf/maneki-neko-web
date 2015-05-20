from django.contrib import admin
from django.db.models import TextField
from django.forms import ModelForm
from djangocms_text_ckeditor.widgets import TextEditorWidget

from news.models import Story


class StoryForm(ModelForm):
    class Meta:
        model = Story

class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'publish_date')
    list_filter = ('status', 'publish_date')
    form = StoryForm
    formfield_overrides = {
        TextField: {'widget': TextEditorWidget}                           
    }
    ordering = ['status', '-publish_date', '-id']
    radio_fields = {"status": admin.HORIZONTAL}
    search_fields = ['title', 'content']              

admin.site.register(Story, StoryAdmin)
