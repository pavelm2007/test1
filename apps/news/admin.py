from django.contrib import admin
from django.forms.widgets import Textarea
from .models import *


class NewAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            kwargs['widget'] = Textarea
        return super(NewAdmin, self).formfield_for_dbfield(db_field, **kwargs)


admin.site.register(New, NewAdmin)

admin.site.register(Like)