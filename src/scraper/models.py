from django.db import models

class City(models.Model):
   name = models.CharField(max_length = 50, verbose_name = 'Название города', unique = True)
   slug = models.CharField(max_length = 50, blank = True, unique = True)

   class Meta:
      verbose_name = 'Название города1'
      verbose_name_plural = 'Название города2'

   def __str__(self):
      return self.name
   
class Language(models.Model):
   name = models.CharField(max_length = 50, verbose_name = 'Язык программирования', unique = True)
   slug = models.CharField(max_length = 50, blank = True, unique = True)

   class Meta:
      verbose_name = 'Язык программирования1'
      verbose_name_plural = 'Языки программирования2'

   def __str__(self):
      return self.name