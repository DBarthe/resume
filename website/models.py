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
  icon = models.FileField(null=True, blank=True, verbose_name=_('icon'))
  icon_attribution = models.URLField(null=True, blank=True, verbose_name=_("a link to the author's website"),
    help_text=_('set it if the license requires it'))

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
  year_to = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('ending year'),
    help_text=_('the year when the job ended, otherwise leave it blank'))

  def get_translation_set(self):
    return self.experiencetranslation_set

  def __unicode__(self):
    return self.employer

class ExperienceTranslation(AbstractTranslation):
  experience = models.ForeignKey(Experience)
  title = models.CharField(max_length=255, verbose_name=_('title'))

class ExperienceTask(models.Model):
  experiencetranslation = models.ForeignKey(ExperienceTranslation)
  description = models.TextField(verbose_name=_('description'), 
    help_text=_('Some lines that describe how the task was amazing !'))

  def __unicode__(self):
    return self.description[:40] + "..."


class Education(AbstractMultilingual):
  year_from = models.PositiveIntegerField(verbose_name=_('start year'), 
    help_text=_('the year when the formation began'))
  year_to = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('ending year'),
    help_text=_('the year when the formation ended, otherwise leave it blank'))

  def get_translation_set(self):
    return self.educationtranslation_set

  def __unicode__(self):
    return (str(self.get_translation('en')) or _("No description"))

class EducationTranslation(AbstractTranslation):
  education = models.ForeignKey(Education)
  school = models.CharField(max_length=255, verbose_name=_('school'))
  title = models.CharField(max_length=255, verbose_name=_('title'))

  def __unicode__(self):
    return self.school


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

class Profile(AbstractMultilingual):
  date = models.DateTimeField(auto_now_add=True)

  picture = models.FileField(null=True, blank=True, verbose_name=_('picture'))

  firstname = models.CharField(max_length=31, verbose_name=_('first name'))
  lastname = models.CharField(max_length=31, verbose_name=_('last name'))
  birthdate = models.DateField(verbose_name=_('birth date'))

  email = models.EmailField(verbose_name=_('email address'))
  phone = models.CharField(max_length=31, verbose_name=_('phone number'))

  street_address = models.CharField(max_length=255, verbose_name=_('street address'))
  zip_code = models.CharField(max_length=15, verbose_name=_('zip code'))
  city = models.CharField(max_length=31, verbose_name=_('city name'))
  country = models.CharField(max_length=31, verbose_name=_('country name'))

  github = models.URLField(verbose_name=_('url of the github account'))

  def get_translation_set(self):
    return self.profiletranslation_set

  def __unicode__(self):
    return self.firstname + " " + self.lastname

  def age(self):
      from datetime import date
      today = date.today()
      born = self.birthdate
      return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

class ProfileTranslation(AbstractTranslation):
  profiles = models.ForeignKey(Profile)
  title = models.CharField(max_length=255, verbose_name=_('title'),
    help_text=_('current position in life (ex: student...)'))