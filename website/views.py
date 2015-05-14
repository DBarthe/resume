from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.translation import npgettext
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import TechnicalSkill as TechSkill, Extra, Skill, Experience, Education, Profile

class Index(TemplateView):
  template_name = 'website/index.html'

  @method_decorator(ensure_csrf_cookie)
  def dispatch(self, *args, **kwargs):
    return super(Index, self).dispatch(*args, **kwargs)

  def get_context_data(self, **kwargs):
    context = super(Index, self).get_context_data(**kwargs)
    context['tech_skill_category_list'] = self.make_tech_skill_category_list()
    context['skill_list'] = self.make_skill_list()
    context['experience_list'] = self.make_experience_list()
    context['education_list'] = self.make_education_list()
    context['extra_list'] = self.make_extra_list()
    context['profile'] = self.get_profile()   
    return context

  def make_tech_skill_category_list(self):
    full_tech_skill_list = TechSkill.objects.order_by('-weight')
    language_list = full_tech_skill_list.filter(category=TechSkill.LANGUAGE)
    framework_list = full_tech_skill_list.filter(category=TechSkill.FRAMEWORK)
    system_list = full_tech_skill_list.filter(category=TechSkill.SYSTEM)
    software_list = full_tech_skill_list.filter(category=TechSkill.SOFTWARE)
    database_list = full_tech_skill_list.filter(category=TechSkill.DATABASE)
    other_list = full_tech_skill_list.filter(category=TechSkill.OTHER)
    return [
      { 'list': language_list,
        'label': npgettext('category', 'Programming Language', 'Programming Languages', len(language_list)) },
      { 'list': framework_list,
        'label': npgettext('category', 'Framework', 'Frameworks', len(framework_list)) },
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

  def make_education_list(self):
    return self.make_translated_list(Education.objects.order_by('-year_from'))

  def make_extra_list(self):
    return self.make_translated_list(Extra.objects.order_by('-weight'))

  def get_profile(self):
    query = Profile.objects.order_by('-date').first()
    if query is None:
      return None # let's see what happens (should not be reached if database is fully completed)
    else:
      fake_queryset = [query] # to use self.make_translated_list
      result_list = self.make_translated_list(fake_queryset)
      return (result_list[0] if result_list else None)


class Sitemap(TemplateView):
  template_name = 'website/sitemap.xml'

  def get(self, request, *args, **kwargs):
    context = self.get_context_data()
    return self.render_to_response(context, content_type="text/xml; charset=utf-8")
