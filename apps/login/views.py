from django.shortcuts import render_to_response
from django.template.context import RequestContext

def index(request):
   context = RequestContext(request, {'user': request.user})
   return render_to_response('login/index.html', context_instance=context)
