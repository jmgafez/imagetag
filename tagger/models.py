# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.template import defaultfilters
from unique_slugify import unique_slugify
import uuid


def upload_to_images(instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid.uuid4().hex, ext)
        return '%s/%s' % (instance.__class__.__name__, filename)


class TimestampedModel(models.Model):
    creation_date = models.DateTimeField(
        _('creation date'), auto_now_add=True)
    last_update = models.DateTimeField(_('last update'), auto_now=True)

    class Meta:
        abstract = True


class SlugifyModel(models.Model):
    slug = models.SlugField(_('slug'), blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug or "slug" in kwargs:
            self.slug = defaultfilters.slugify(self.__unicode__())
        unique_slugify(self, self.slug)
        super(SlugifyModel, self).save(*args, **kwargs)


class ImageT(TimestampedModel, SlugifyModel):
    user = models.ForeignKey(
        User, verbose_name=_('user'), on_delete=models.CASCADE
    )
    image = models.ImageField(_('image'), upload_to=upload_to_images)

    class Meta:
        verbose_name = _('image')
        verbose_name_plural = _('images')

    def __unicode__(self):
        return self.image.name


class Tag(TimestampedModel, SlugifyModel):
    name = models.CharField(_('name'), max_length=256, unique=True)
    images = models.ManyToManyField(
        ImageT, verbose_name=_('image'), related_name='tags')

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')

    def __unicode__(self):
        return self.name
