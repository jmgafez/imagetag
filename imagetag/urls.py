# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from tagger import urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),

    url(r'', include(urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
