from django.shortcuts import render_to_response, HttpResponse, redirect, render
from django.template.context import RequestContext
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
import tweepy
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
	consumer_key = '7wNNbY73FH1zy3CF1YTfEcUql'
	consumer_secret = 'RqnFtaBOTmpsqR1WjJSf8icSVYpUYbxp1UeBUxTI0uMnXOYkGI'
	access_token = '237866783-1xllrhSJFKRuxoXwZ0MOJStLrjnm79uNS1I51uew'
	access_token_secret = 'fEiXcsH0UDfEXWu87vEt5O9Pve8CRCoERna0ydfSPecWP'
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

	# try:
	# 	redirect_url = auth.get_authorization_url()
	# except tweepy.TweepError:
	# 	print 'Error! Failed to get request token.'
	# request.session['request_token'] = auth.request_token
	# verifier = request.GET.get('oauth_verifier')
	# auth = tweepy.OAuthHandler(consumer_key, consumer_token)
	# token = request.session['request_token']
	# del request.session['request_token']
	# auth.request_token = token

	# try:
	# 	auth.get_access_token(verifier)
	# except tweepy.TweepError:
	# 	print 'Error! Failed to get access token.'


	
	# auth = tweepy.OAuthHandler(consumer_key, consumer_token)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	# api.update_status('tweepy + oauth!')
	tweets = api.search(geocode="47.60994,-122.19666,4mi")
	context = RequestContext(request, {'request': request, 'user':request.user, 'tweets': tweets})
	return render_to_response('login/dashboard.html', context_instance=context)
