# -*- coding: utf-8 -*-
__author__ = 'marvin'

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render_to_response('base/index.html', context_instance=RequestContext(request))
