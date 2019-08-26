# Create your views here.
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .weather import WeatherApi

def index(request):
  if request.user.is_authenticated:
    weatherApi = WeatherApi('https://api.openweathermap.org/data/2.5/weather','44353e2bc29c022d20a1b3cdccdc41fc')
    if 'postalCode' in request.GET:
      weather = weatherApi.getWeatherDetails(request.GET['postalCode'])
    else:
      weather = weatherApi.getWeatherDetails('7500')
    return render(request, 'index.html', {'weather': weather})
  else:
    return render(request, 'registerOrLogin.html')

def register(request):
  # Try to auth them
  user = authenticate(username=request.POST['username'], password=request.POST['password'])
  if user is None:
    User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
  # Login after registration
  user = authenticate(username=request.POST['username'], password=request.POST['password'])
  auth_login(request, user)
  return redirect('/api')

def login(request):
  user = authenticate(username=request.POST['username'], password=request.POST['password'])
  if user is not None:
    auth_login(request, user)
    return redirect('/api')
  else:
    return redirect('/api/login')

def logout(request):
  auth_logout(request)
  return redirect('/api/')
