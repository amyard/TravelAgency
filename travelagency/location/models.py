from django.db import models
from django.utils.translation import ugettext_lazy as _



class Country(models.Model):
    title = models.CharField(max_length = 50)
    title_en = models.CharField(max_length=50)
    title_de = models.CharField(max_length=50)


    slug = models.SlugField(max_length = 50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')