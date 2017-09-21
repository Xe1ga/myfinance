from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


# Create your models here.
def getnow():
    return timezone.now()

class MetersData(models.Model):
	date_meter = models.DateField(verbose_name = 'Дата снятия показаний', default = getnow)
	cold_water = models.DecimalField(max_digits = 10, decimal_places = 3, verbose_name = 'Холодная вода')
	hot_water = models.DecimalField(max_digits = 10, decimal_places = 3, verbose_name = 'Горячая вода')
	electricity_apartment = models.DecimalField(max_digits = 10, decimal_places = 3, verbose_name = 'Электричество в квартире')
	electricity_storeroom = models.DecimalField(max_digits = 10, decimal_places = 3, verbose_name = 'Электричество в подсобном помещении')
	note = models.CharField(max_length = 200, verbose_name = 'Примечание', blank = True)
	class Meta:
		ordering = ["-date_meter"]
	def get_absolute_url(self):
		return reverse ('meters:index', )