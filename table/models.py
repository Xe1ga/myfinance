from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

# Create your models here.
def getnow():
    return timezone.now()

class Typeofbuy(models.Model): #create table Typeofbuy (tip pokupki)
    typeofbuy_text = models.CharField(max_length = 200, verbose_name = 'Тип расхода')
    def __str__(self):
    	return self.typeofbuy_text
    def get_absolute_url(self):
        return reverse ('table:typeofcost', )

class Costs(models.Model): #create table Costs (rasxody)
    date_buy = models.DateTimeField(verbose_name = 'Дата покупки', default = getnow , help_text = 'гггг-мм-дд')
    summa_buy = models.DecimalField(max_digits = 9, decimal_places = 2, verbose_name = 'Сумма покупки')
    type_of_buy = models.ForeignKey(Typeofbuy, on_delete = models.CASCADE, verbose_name = 'Тип покупки') #eto id typeofbuy
    note = models.CharField(max_length = 200, verbose_name = 'Примечание', blank = True)
    class Meta:
        ordering = ["-date_buy"]
    def get_absolute_url(self):
        return reverse ('table:addcost', )

class Typeofincome(models.Model): #create table Typeofincome (tip doxoda)
    typeofincome_text = models.CharField(max_length = 200)   
    def __str__(self):
    	return self.typeofincome_text
    def get_absolute_url(self):
        return reverse ('table:typeofcost', )

class Incomes(models.Model): #create table Incomes (doxody)
    date_income = models.DateTimeField()
    summa_income = models.DecimalField(max_digits = 9, decimal_places = 2)
    type_of_income = models.ForeignKey(Typeofincome, on_delete = models.CASCADE) #eto id typeofbuy
    note = models.CharField(max_length = 200)

