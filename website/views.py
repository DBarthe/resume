from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.translation import npgettext

from .models import TechnicalSkill as TechSkill, Extra
from .models import Skill
from .models import Experience

class Index(TemplateView):
  template_name = 'website/index.html'

  def get_context_data(self, **kwargs):
    context = super(Index, self).get_context_data(**kwargs)
    context['tech_skill_category_list'] = self.make_tech_skill_category_list()
    context['skill_list'] = self.make_skill_list()
    context['experience_list'] = self.make_experience_list()
    context['extra_list'] = self.make_extra_list()
    return context

  def make_tech_skill_category_list(self):
    full_tech_skill_list = TechSkill.objects.order_by('-weight')
    language_list = full_tech_skill_list.filter(category=TechSkill.LANGUAGE)
    system_list = full_tech_skill_list.filter(category=TechSkill.SYSTEM)
    software_list = full_tech_skill_list.filter(category=TechSkill.SOFTWARE)
    database_list = full_tech_skill_list.filter(category=TechSkill.DATABASE)
    other_list = full_tech_skill_list.filter(category=TechSkill.OTHER)
    return [
      { 'list': language_list,
        'label': npgettext('category', 'Programming Language', 'Programming Languages', len(language_list)) },
      { 'list': system_list,
        'label': npgettext('category', 'Operating System', 'Operating Systems', len(system_list)) },
      { 'list': software_list,
        'label': npgettext('category', 'Software', 'Softwares', len(software_list)) },
      { 'list': database_list,
        'label': npgettext('category', 'Database', 'Databases', len(database_list)) },
      { 'list': other_list,
        'label': npgettext('category', 'Other', 'Others', len(other_list)) },
    ]

  def make_translated_list(self, queryset):
    language = self.request.LANGUAGE_CODE
    def helper(obj):
      obj.translation = obj.get_translation(language)
      return obj
    return [helper(obj) for obj in queryset]

  def make_skill_list(self):
    return self.make_translated_list(Skill.objects.order_by('-weight'))

  def make_experience_list(self):
    return self.make_translated_list(Experience.objects.order_by('-year_from'))

  def make_extra_list(self):
    return self.make_translated_list(Extra.objects.order_by('-weight'))
