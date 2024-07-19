from django.contrib import admin

from .models import Record


class RecordAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "phone", "city", "country"]


admin.site.register(Record, RecordAdmin)
