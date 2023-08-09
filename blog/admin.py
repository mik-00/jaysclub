from django.contrib import admin

from . import models

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(models.Posts, PostAdmin)