#!/usr/bin/env python
# coding: utf-8
#from django.template.loader import get_template
from django.http import HttpResponse, Http404
from django.template import Template, Context
import time
import datetime
from django.shortcuts import render_to_response

def hello(request):
    return HttpResponse("Hello World")

def current_time(request):
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    #t = get_template('current_datetime.html')
    #html = t.render(Context({'current_date': now}))
    #return HttpResponse(html)
    return render_to_response('current_datetime.html', {'current_date': now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #assert False
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
