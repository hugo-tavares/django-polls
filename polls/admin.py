# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Question, Choice

# Question objects have an admin interface
admin.site.register(Question)

admin.site.register(Choice)
