from django.shortcuts import render_to_response, HttpResponse, redirect, render
from django.template.context import RequestContext
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

def index(request):
    context = RequestContext(request, {'user': request.user})
    return render_to_response('login/index.html', context_instance=context)

def login(request):
    return render(request, 'login/dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def home(request):
    context = RequestContext(request, {'request': request, 'user': request.user})
    return render_to_response('login/home.html', context_instance=context)

@login_required(login_url='/home')
def dashboard(request):
    return render_to_response('login/dashboard.html')
