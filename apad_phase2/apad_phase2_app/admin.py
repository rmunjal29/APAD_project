# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import add_venue, add_new_event

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(add_venue)
admin.site.register(add_new_event)
