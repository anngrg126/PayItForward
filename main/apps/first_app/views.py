# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited

def index(request):
	context = {
		"email" : "blog@gmail.com", 
		"name" : "mike"
	}
	return render(request, "first_app/index.html", context)

#def index(request):
#	response = "Hello, I am your first request!"
#	return HttpResponse(response)

