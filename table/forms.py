import datetime
from django import forms
from .models import Costs, Typeofbuy
from django.forms import ModelForm, Form
from django.utils import timezone
from datetime import date

class LoginForm(forms.Form):
    username = forms.CharField(label="Имя пользователя", max_length=256, required=True)
    password = forms.CharField(label="Пароль", max_length=256, widget=forms.PasswordInput, required=True)
    
class CostsForm(ModelForm): #создание формы из модели
	class Meta:
		model = Costs
		fields = ['date_buy', 'type_of_buy', 'summa_buy', 'note']
		error_css_class = 'error'
		required_css_class = 'required'

class InputDateForm(Form): # создание формы вручную
	from_date = forms.DateTimeField(label = 'Введите начальную дату', help_text = 'гггг-мм-дд', initial = datetime.date(timezone.now().year, timezone.now().month, 1))
	due_date = forms.DateTimeField(label = 'Введите конечную дату', help_text = 'гггг-мм-дд', initial = timezone.now())
	error_css_class = 'error'
	required_css_class = 'required'

class TypeOfCostsForm(ModelForm):
	class Meta:
		model = Typeofbuy
		fields = ['typeofbuy_text']
		error_css_class = 'error'
		required_css_class = 'required'