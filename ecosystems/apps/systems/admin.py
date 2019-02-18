from typing import List

from django.contrib import admin
from ecosystems.apps.systems.models import Accesses


# Register your models here.
class AccessesAdmin(admin.ModelAdmin):
    list_display = ('owner', 'title', 'service', 'comment', 'id')


admin.site.register(Accesses, AccessesAdmin)
