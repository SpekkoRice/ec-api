# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question
from .models import Choice
from django.template import loader
from django.urls import reverse


def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  template = loader.get_template('index.html')
  # return render(request, 'polls/index.html', context)
  context = {
      'latest_question_list': latest_question_list,
  }
  return HttpResponse(template.render(context, request))

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
    return HttpResponseRedirect(reverse('api:results', args=(question.id,)))
