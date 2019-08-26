# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from .weather import WeatherApi

from .models import Question, Choice

def index(request):
  weatherApi = WeatherApi(
    'https://api.openweathermap.org/data/2.5/weather',
    '44353e2bc29c022d20a1b3cdccdc41fc'
  )
  weather = weatherApi.getWeatherDetails(request.GET['postalCode'])
  # print(dir(weather))
  return render(request, 'index.html', {'weather': weather})

def detail(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/details.html', {'question': question})

def results(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
  return HttpResponse("You're voting on question %s." % question_id)

def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    # Redisplay the question voting form.
    return render(request, 'polls/details.html', {
        'question': question,
        'error_message': "You didn't select a choice.",
    })
  else:
    selected_choice.votes += 1
    selected_choice.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('api  :results', args=(question.id,)))

