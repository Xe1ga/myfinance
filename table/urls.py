from django.conf.urls import url

from . import views

app_name = 'table'
urlpatterns = [
    # ex: /table/main основная страница
    url(r'^$', views.main, name = 'main'),
     # ex: /table/auth_login/ аутентификация
    url(r'^auth_login/$', views.auth_login, name='auth_login'),
     # ex: /table/auth_logout/ выход из системы
    url(r'^auth_logout/$', views.auth_logout, name='auth_logout'),
    # ex: /table/costlist/   таблица расходов за текущий месяц
    url(r'^costslist/$', views.current_month_expenses, name = 'current_month_expenses'),
    # ex: /table/addcost/   добавить расход
    url(r'^addcost/$', views.AddCostView.as_view(), name = 'addcost'),
    # ex: /table/costsample/   поиск по расходам
    url(r'^costssample/$', views.get_costs_sample, name = 'costssample'),
    # ex: /table/costsample/2 редактирование существующего расхода
    url(r'^costssample/(?P<cost_id>[0-9]+)/$', views.get_change_cost, name = 'getchangecost'),
    # ex: /table/typeofcosts/ типы расходов
    url(r'^typeofcosts/$', views.AddTypeOfCostView.as_view(), name = 'typeofcost'),
    
]