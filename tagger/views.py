# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ImageForm, SearchTagForm
from .models import ImageT, Tag


@method_decorator(login_required, name='dispatch')
class FrontendView(View):
    template_name = ""
    extra_context = {}

    def get(self, request, **kwargs):
        return render(request, self.template_name, self.extra_context)


class ImagesView(FrontendView):
    template_name = "tagger/images.html"
    extra_context = {
        "images": ImageT.objects.all().order_by('-creation_date')
    }


class UploadImageView(FrontendView):
    template_name = "tagger/upload_image.html"

    def get(self, request, **kwargs):
        self.extra_context = {
            "form": ImageForm({"user": request.user})
        }

        return super(UploadImageView, self).get(request, **kwargs)

    def post(self, request, **kwargs):
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            image_t = form.save()
            return redirect(reverse('show_image', args=(image_t.id,)))
        else:
            self.extra_context = {
                "form": form
            }

        return render(request, self.template_name, self.extra_context)


class ShowImageView(FrontendView):
    template_name = "tagger/show_image.html"

    def get(self, request, **kwargs):
        self.extra_context = {
            "image_t": get_object_or_404(ImageT, id=kwargs['id'])
        }

        return super(ShowImageView, self).get(request, **kwargs)


class ShowTagView(FrontendView):
    template_name = "tagger/show_tag.html"

    def get(self, request, **kwargs):
        self.extra_context = {
            "tag": get_object_or_404(Tag, id=kwargs['id'])
        }

        return super(ShowTagView, self).get(request, **kwargs)


class SearchTagsView(FrontendView):
    template_name = "tagger/search_tags.html"
    extra_context = {
        "tags": None
    }

    def post(self, request, **kwargs):
        form = SearchTagForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            self.extra_context = {
                "tags": Tag.objects.filter(name__contains=name)
            }

        return render(request, self.template_name, self.extra_context)
