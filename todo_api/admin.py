from django.contrib import admin

from todo_api.models import TODO, AppUser

# Register your models here.
admin.site.register(AppUser)
admin.site.register(TODO)
