from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import *

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UserProfileInLine(admin.StackedInline):
    model = user_profile
    can_delete = False
    verbose_name_plural = 'profile'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInLine, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(add_venue)
admin.site.register(add_event_cat)
admin.site.register(add_sports)
admin.site.register(add_new_event)