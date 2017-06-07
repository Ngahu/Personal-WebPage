# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.template import loader


class HomePage(View):
    """
    this views returns the basic homepage the home of the webpage
    """
    def get(self,request):
        template = loader.get_template('Home/index.html')
        return HttpResponse(template.render(request))
        #return HttpResponse("hello Champ")