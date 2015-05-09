from django.shortcuts import render
from django.views.generic import View, ListView

from .models import TechnicalSkill

class Index(ListView):
  model = TechnicalSkill
  template_name = 'website/index.html'

