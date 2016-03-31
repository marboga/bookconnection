from django.shortcuts import render_to_response, HttpResponse, redirect
from django.template.context import RequestContext
from django.contrib.auth import login, logout, authenticate

def index(request):
    context = RequestContext(request, {'user': request.user})
    return render_to_response('login/index.html', context_instance=context)

def login(request):
    return HttpResponse('towkrorktedd')

def logout_view(request):
    logout(request)
    return redirect('home')

def home(request):
    context = RequestContext(request, {'request': request, 'user': request.user})
    return render_to_response('login/home.html', context_instance=context)
