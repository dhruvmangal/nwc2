from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render, redirect, HttpResponseRedirect
from django.http import HttpResponse, Http404

def Home(request):
    return redirect("/app/")