from django.shortcuts import render_to_response, HttpResponse, redirect, render
from django.template.context import RequestContext
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

def index(request):
	print "index"
	context = RequestContext(request, {'user': request.user})
	return render_to_response('login/index.html', context_instance=context)

def login(request):
	print "login"
	return render(request, 'login/dashboard.html')

def logout_view(request):
	print "logout"
	logout(request)
	return redirect(home)

def home(request):
	print "home"
	context = RequestContext(request, {'request': request, 'user': request.user})
	return render_to_response('login/home.html', context_instance=context)

@login_required(login_url='home')
def dashboard(request):
	print "dashboard"
	return render_to_response('login/dashboard.html')
