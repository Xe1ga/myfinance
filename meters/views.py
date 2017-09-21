from django.shortcuts import render
from django.views import generic
from django.db import connection #модуль для обращения напрямую к БД
from django.shortcuts import get_list_or_404, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import *
from .forms import *

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

@login_required(login_url='/table/')
def index(request):
	current_year = timezone.now().year
	# запрос через manager django
	meters_current_year = MetersData.objects.filter(date_meter__year = current_year)
	context = {'meters_current_year': meters_current_year}
	return render(request, 'meters/meterscurrentyear.html', context)

class AddMetersDataView(LoginRequiredMixin, PermissionRequiredMixin, generic.edit.CreateView): # добавление нового расхода по ссылке главного меню
	model = MetersData
	fields = ['date_meter', 'cold_water', 'hot_water', 'electricity_apartment', 'electricity_storeroom', 'note']
	template_name = 'meters/addmetersdata.html'
	login_url = '/table/'
	permission_required = 'meter.add_metersdata'
	#url для редиректа определен в модели

@permission_required('meter.change_metersdata', login_url='/table/')
@login_required(login_url='/table/')
def get_change_meter(request, meter_id): # изменение конкретного существующего расхода по ссылке из таблицы
	meter = get_object_or_404(MetersData, pk = meter_id)
	if request.method == 'POST':
		form = MetersForm(request.POST, instance = meter) # связывание данных формы с данными конкретного экземпляра модели  (изменение)
		form.save() 
		return HttpResponseRedirect(reverse('meters:index', ))
	else:
		form = MetersForm(instance = meter) # создание формы для изменения существующего расхода
		context = {'form' : form}
		return render(request, 'meters/addmetersdata.html', context)


@login_required(login_url='/table/')
def delete_meter(request, meter_id):
	meter = get_object_or_404(MetersData, pk = meter_id)
	meter.delete()
	return HttpResponseRedirect(reverse('meters:index', ))

@login_required(login_url='/table/')
def get_text_to_send(request): # формирование текста для отправки показаний счетчиков
	with connection.cursor() as cursor:
		sql = """
		SELECT * 
		FROM meters_metersdata
		WHERE date_meter = (SELECT MAX(date_meter) FROM meters_metersdata)
		"""
		cursor.execute(sql)
		meter = dictfetchall(cursor)
	context = {'meter':meter[0]}
	return render(request, 'meters/texttosend.html', context)
