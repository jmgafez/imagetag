# -*- encoding: utf-8 -*-
from django.conf.urls import url
from views import *

urlpatterns = (
    url(r'^$', ImagesView.as_view(), name="images"),
    url(r'^upload_image/$', UploadImageView.as_view(), name="upload_image"),
    url(r'^show_image/(?P<id>\d+)/$',
        ShowImageView.as_view(), name="show_image"),
    url(r'^show_tag/(?P<id>\d+)/$',
        ShowTagView.as_view(), name="show_tag"),
    url(r'^search_tags/$',
        SearchTagsView.as_view(), name="search_tags"),
)
