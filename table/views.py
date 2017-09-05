from django.shortcuts import get_list_or_404, render, get_object_or_404
import datetime
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import *
from django.utils import timezone
from django.views import generic
from .forms import CostsForm, InputDateForm, TypeOfCostsForm
from datetime import date


def main(request):
	context = {}
	return render(request, 'table/main.html', context)

def current_month_expenses(request):
	current_month = timezone.now().month 
	current_year = timezone.now().year
	#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!.order_by("-date_buy")
	#top_costs = get_list_or_404(Costs, date_buy__year = current_year, date_buy__month = current_month)
	top_costs = Costs.objects.filter(date_buy__year = current_year, date_buy__month = current_month)
	#cost_list = [str(el.date_buy)[:10] + " " + str(el.summa_buy) + " " + str(el.type_of_buy) for el in top_costs]
	context = {'top_costs': top_costs}
	return render(request, 'table/lastcosts.html', context)


class AddCostView(generic.edit.CreateView): # добавление нового расхода по ссылке главного меню
	model = Costs
	fields = ['date_buy', 'type_of_buy', 'summa_buy', 'note']
	template_name = 'table/addcost.html'
	#url для редиректа определен в модели
	

class AddTypeOfCostView(generic.edit.CreateView): # добавление нового  типа расхода по ссылке главного меню
	model = Typeofbuy
	fields = ['typeofbuy_text']
	template_name = 'table/typeofcost.html'
	def get_context_data(self, **kwargs):
		context = super(AddTypeOfCostView, self).get_context_data(**kwargs)
		context['all_types'] = Typeofbuy.objects.order_by('typeofbuy_text')
		return context
	#url для редиректа определен в модели 

'''def get_delete_or_change_type_of_cost(request): # изменение или удаление типа расхода 
	all_types = Typeofbuy.objects.order_by('typeofbuy_text')
	if request.method == 'POST':
		form = TypeOfCostsForm(request.POST)
		form.save() 
	else:
		form = TypeOfCostsForm() 
	context = {'form' : form, 'all_types':all_types if all_types else None}
	return render(request, 'table/typeofcost.html', context)
'''
def get_costs_sample(request): # выборка расходов по датам
	costs_sample_list = []
	start_date = datetime.date(timezone.now().year,1,1)
	end_date = timezone.now()
	if request.method == 'POST':
		form = InputDateForm(request.POST)
		if form.is_valid():
			start_date = form.cleaned_data['start_date']
			end_date = form.cleaned_data['end_date']
			costs_sample_list = Costs.objects.filter(date_buy__range = (start_date, end_date))
	else:
		form = InputDateForm()
	context = {'form' : form, 'costs_sample_list': costs_sample_list if costs_sample_list else None, 'start_date':start_date, 'end_date':end_date}
	return render(request, 'table/costssample.html', context)

def get_change_cost(request, cost_id): # изменение конкретного существующего расхода по ссылке из таблицы
	cost = get_object_or_404(Costs, pk = cost_id)
	if request.method == 'POST':
		form = CostsForm(request.POST, instance = cost) # связывание данных формы с данными конкретного экземпляра модели  (изменение)
		form.save() 
		return HttpResponseRedirect(reverse('table:current_month_expenses', ))
	else:
		form = CostsForm(instance = cost) # создание формы для изменения существующего расхода
		context = {'form' : form}
		return render(request, 'table/addcost.html', context)

