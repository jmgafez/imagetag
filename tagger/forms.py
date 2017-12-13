# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib.auth.models import User
from .models import ImageT, Tag
from .google_vision import get_image_labels


class ImageForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=None)

    class Meta:
        model = ImageT
        fields = ['user', 'image']

    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        self.fields['user'].widget = forms.HiddenInput()

    def save(self):
        image_t = super(ImageForm, self).save()
        labels = get_image_labels(image_t.image.path)

        for label in labels:
            try:
                tag = Tag.objects.get(name=label.description)
            except Exception:
                tag = Tag.objects.create(
                    name=label.description,
                )
            tag.images.add(image_t)

        return image_t


class SearchTagForm(forms.Form):
    name = forms.CharField(required=True)
