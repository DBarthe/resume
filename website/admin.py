from django.contrib import admin

from .models import TechnicalSkill, Skill, SkillTranslate

class SkillTranslateInline(admin.StackedInline):
  model = SkillTranslate
  min_num = 2
  extra = 0

class SkillAdmin(admin.ModelAdmin):
  inlines = [SkillTranslateInline]

admin.site.register(TechnicalSkill)
admin.site.register(Skill, SkillAdmin)