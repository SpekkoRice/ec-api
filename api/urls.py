from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
  # ex: /api/
  path('', views.index, name='index'),
  ### THESE CAN BE DELETED
  # ex: /api/5/
  path('<int:question_id>/', views.detail, name='detail'),
  # ex: /api/5/results/
  path('<int:question_id>/results/', views.results, name='results'),
  # ex: /api/5/vote/
  path('<int:question_id>/vote/', views.vote, name='vote'),

  ### Login endpoints should be there
]