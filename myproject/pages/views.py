# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Post
# Create your views here.
from django.views.generic import TemplateView,ListView


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'
class PostPageView(ListView):
    model = Post
    template_name = 'posts.html'
