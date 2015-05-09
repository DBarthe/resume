from django.db import models
from django.utils.translation import ugettext_lazy as _

class TechnicalSkill(models.Model):
  LANGUAGE = 'LA'
  SYSTEM = 'SY'
  DATABASE = 'DA'
  SOFTWARE = 'SO'
  OTHER = 'OT'
  CATEGORY_CHOICES = (
    (LANGUAGE, _('Language')),
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
