# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ImageT, Tag

admin.site.register(ImageT)
admin.site.register(Tag)
