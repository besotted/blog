from __future__ import unicode_literals
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from postapp.models import *
admin.site.register(stopic)
admin.site.register(blog_type)
admin.site.register(postblog)
