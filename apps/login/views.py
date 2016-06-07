from django.shortcuts import render_to_response, HttpResponse, redirect, render
from django.template.context import RequestContext
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
import tweepy
import re
from bookconnection import config

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
	# these are our thingys for twitter
	consumer_key = 'lvkxdMrGwgi31uBQiI1xeWcvh'
	consumer_secret = 'a6lOPq812jbpuqAJQNuZR0NcpALb5C5i55TM6oxDUpk2iCWIdt'
	access_token = '3259568774-QpD37XpTQ3VIywnF2HnzBPkjGeQBGbbdtRiSqPD'
	access_token_secret = 'Yvf8cxPcVjqPYQtMq673qhDglKfOYjVVggfOKaLtlYHL7'
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth, wait_on_rate_limit_notify=True)
	# api.update_status("I just finished a 24 hour hackathon!")
	tweets = api.search(count="100",geocode="47.60994,-122.19666,1mi")
	context = RequestContext(request, {'request': request, 'user':request.user, 'tweets': tweets})
	return render_to_response('login/dashboard.html', context_instance=context)
