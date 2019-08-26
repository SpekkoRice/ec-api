from django.db import models

class User(models.Model):
  username = models.CharField(max_length=200, blank=False)
  password = models.CharField(max_length=200, blank=False)
  email = models.EmailField(max_length=200, blank=False)
  first_name = models.CharField(max_length=200, blank=True)
  last_name = models.CharField(max_length=200, blank=True)
  timestamp = models.DateTimeField('date published')
  def __str__(self):
    return self.name
