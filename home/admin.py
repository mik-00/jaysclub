from django.contrib import admin

from . import models

class ReportAdmin(admin.ModelAdmin):
    list_display = ("title",)

admin.site.register(models.Reports, ReportAdmin)