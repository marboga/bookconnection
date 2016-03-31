from django.shortcuts import render_to_response, HttpResponse
from django.template.context import RequestContext

def index(request):
   context = RequestContext(request, {'user': request.user})
   return render_to_response('login/index.html', context_instance=context)

def login(request):
    return HttpResponse('towkrorktedd')

def logout(request):
    return HttpResponse('towedd')

def home(request):
    context = RequestContext(request, {'request': request, 'user': request.user})
    return render_to_response('login/home.html', context_instance=context)
