from django.conf.urls import url

from . import views

app_name = 'meters'
urlpatterns = [
    # ex: /meters/ основная страница
    url(r'^$', views.index, name = 'index'),
    # ex: /meters/addmetersdata основная страница
    url(r'^addmetersdata/$', views.AddMetersDataView.as_view(), name = 'addmetersdata'),
    url(r'^changemeter/(?P<meter_id>[0-9]+)/$', views.get_change_meter, name = 'getchangemeter'),
    url(r'^deletemeter/(?P<meter_id>[0-9]+)/$', views.delete_meter, name = 'deletemeter'),
    url(r'^texttosend/$', views.get_text_to_send, name = 'texttosend'),
]
