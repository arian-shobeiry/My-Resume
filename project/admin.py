from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.music)
admin.site.register(models.site)
admin.site.register(models.inbox)