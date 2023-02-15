from django.contrib import admin

# Register your models here.
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')


admin.site.register(Link, LinkAdmin)