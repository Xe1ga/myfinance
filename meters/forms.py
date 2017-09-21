import datetime
from django import forms
from .models import MetersData
from django.forms import ModelForm
from django.utils import timezone
from datetime import date

class MetersForm(ModelForm): #создание формы из модели
	class Meta:
		model = MetersData
		fields = ['date_meter', 'cold_water', 'hot_water', 'electricity_apartment', 'electricity_storeroom', 'note']
		error_css_class = 'error'
		required_css_class = 'required'