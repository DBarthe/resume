from django.db import models

class TechnicalSkill(models.Model):
  LANGUAGE = 'LA'
  SYSTEM = 'SY'
  DATABASE = 'DA'
  SOFTWARE = 'SO'
  OTHER = 'OT'
  CATEGORY_CHOICES = (
    (LANGUAGE, 'Language'),
    (SYSTEM, 'System'),
    (DATABASE, 'Database'),
    (SOFTWARE, 'Software'),
    (OTHER, 'Other')
  )
  category = models.CharField(
    max_length=2, choices=CATEGORY_CHOICES, default=OTHER)
  name = models.CharField(max_length=255) # no need to translate
  date = models.DateField(auto_now_add=True)
  weight = models.IntegerField(default=0,
    help_text='Will determine the display order, higher first')
  icon = models.FileField(null=True)

  def __unicode__(self):
    return self.default_name

