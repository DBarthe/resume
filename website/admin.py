from django.contrib import admin
from nested_admin import NestedAdmin, NestedStackedInline

from .models import (TechnicalSkill, Skill, SkillTranslation,
  Experience, ExperienceTranslation, ExperienceTask,
  Extra, ExtraTranslation)

class SkillTranslationInline(admin.StackedInline):
  model = SkillTranslation
  min_num = 2
  extra = 0
  inline_classes = ('grp-collapse grp-open',)
  classes = ('grp-collapse grp-open',)


class SkillAdmin(admin.ModelAdmin):
  inlines = [SkillTranslationInline]

class ExperienceTaskInline(NestedStackedInline):
  model = ExperienceTask
  extra = 0
  min_num = 1

class ExperienceTranslationInline(NestedStackedInline):
  model = ExperienceTranslation
  inlines =  [ExperienceTaskInline]
  extra = 0
  min_num = 2
  inline_classes = ('grp-collapse grp-open',)
  classes = ('grp-collapse grp-open',)

class ExperienceAdmin(NestedAdmin):
  inlines = [ExperienceTranslationInline]

class ExtraTranslationInline(admin.StackedInline):
  model = ExtraTranslation
  extra = 0
  min_num = 2
  inline_classes = ('grp-collapse grp-open',)
  classes = ('grp-collapse grp-open',)

class ExtraAdmin(admin.ModelAdmin):
  inlines = [ExtraTranslationInline]

admin.site.register(TechnicalSkill)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Extra, ExtraAdmin)