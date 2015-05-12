from django.db import models
from django.utils.translation import ugettext_lazy as _

class TechnicalSkill(models.Model):
  LANGUAGE = 'LA'
  FRAMEWORK = 'FA'
  SYSTEM = 'SY'
  DATABASE = 'DA'
  SOFTWARE = 'SO'
  OTHER = 'OT'
  CATEGORY_CHOICES = (
    (LANGUAGE, _('Language')),
    (FRAMEWORK, _('Framework')),
    (SYSTEM, _('System')),
    (DATABASE, _('Database')),
    (SOFTWARE, _('Software')),
    (OTHER, _('Other')),
  )
  category = models.CharField(
    max_length=2,
    choices=CATEGORY_CHOICES,
    default=OTHER,
    verbose_name=_('category')
  )
  name = models.CharField(max_length=255, verbose_name=_('name')) # no need to translate
  date = models.DateField(auto_now_add=True, verbose_name=_('date'))
  weight = models.IntegerField(
    default=0,
    verbose_name=_('weight'),
    help_text=_('Will determine the display order, higher first')
  )
  icon = models.FileField(null=True, verbose_name=_('icon'))

  def __unicode__(self):
    return self.name


class AbstractMultilingual(models.Model):
  """ This model is the base of others models
  that have some fields to be translated """

  class Meta:
    abstract = True

  """ To be redefined by child class.
  Must return a queryset of AbstractTranslation """
  def get_translation_set(self):
    raise NotImplementedError("get_translation_set must be implemented")

  """
  Get the Translate object associated with this object and the language.
  If there are several translations, the youngest will be returned.
  If there are no translations, the english will be returned.
  In the last case, if there is no english translation, None is returned
  """
  def get_translation(self, language):
    result = self.get_translation_set().filter(language=language).order_by('-date').first()
    if result is None and language != 'en':
      result = self.get_translation('en')
    return result


class AbstractTranslation(models.Model):
  """ This model is the base of others translation models """

  class Meta:
    abstract = True

  date = models.DateTimeField(auto_now_add=True, verbose_name=_('date'),
  help_text=_('The youngest translation for a language will be selected'))
  language = models.CharField(max_length=5, verbose_name=_('language'),
    help_text=_('The language code (like "en" or "fr")'))


class Skill(AbstractMultilingual):
  date = models.DateField(auto_now_add=True, verbose_name=_('date'))
  weight = models.IntegerField(
    default=0,
    verbose_name=_('weight'),
    help_text=_('Will determine the display order, higher first')
  )

  def get_translation_set(self):
    return self.skilltranslation_set

  def __unicode__(self):
    return ("en: " + str(self.get_translation('en'))[:40] + "...") or _("No description")

class SkillTranslation(AbstractTranslation):
  skill = models.ForeignKey(Skill)
  description = models.TextField(verbose_name=_('description'), 
    help_text=_('A one or two lines description of the skill'))

  def __unicode__(self):
    return self.description


class Experience(AbstractMultilingual):
  employer = models.CharField(max_length=255, verbose_name=_('employer'))
  year_from = models.PositiveIntegerField(verbose_name=_('start year'), 
    help_text=_('the year when the job began'))
  year_to = models.PositiveIntegerField(null=True, verbose_name=_('ending year'),
    help_text=_('the year when the job ended, or null'))

  def get_translation_set(self):
    return self.experiencetranslation_set

  def __unicode__(self):
    return self.employer

class ExperienceTranslation(AbstractTranslation):
  experience = models.ForeignKey(Experience)
  title = models.CharField(max_length=255, verbose_name=_('title'))

  def __unicode__(self):
    return self.title

class ExperienceTask(models.Model):
  experiencetranslation = models.ForeignKey(ExperienceTranslation)
  description = models.TextField(verbose_name=_('description'), 
    help_text=_('Some lines that describe how the task was amazing !'))

  def __unicode__(self):
    return self.description[:40] + "..."

class Extra(AbstractMultilingual):
  date = models.DateField(auto_now_add=True, verbose_name=_('date'))
  weight = models.IntegerField(
    default=0,
    verbose_name=_('weight'),
    help_text=_('Will determine the display order, higher first')
  )

  def get_translation_set(self):
    return self.extratranslation_set

  def __unicode__(self):
    return ("en: " + str(self.get_translation('en'))[:40] + "...") or _("No description")

class ExtraTranslation(AbstractTranslation):
  extra = models.ForeignKey(Extra)
  name = models.CharField(max_length=255, verbose_name=_('name'))
  description = models.TextField(blank=True, verbose_name=_('description'),
    help_text=_('An optional description of this extra'))

  def __unicode__(self):
    return self.name