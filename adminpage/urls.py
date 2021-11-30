from django.conf.urls import url
from adminpage import views

urlpatterns = [
    url(r'^$', views.adminhome, name="adminhome"),
    url(r'^add_asset/$', views.add_asset, name="add_asset"),
    url(r'^add_booking/$', views.add_booking, name="add_booking"),
    url(r'^add_customer/$', views.add_customer, name="add_customer"),
    url(r'^add_employee/$', views.add_employee, name="add_employee"),
    url(r'^add_room/$', views.add_room, name="add_room"),
    url(r'^add_role/$', views.add_role, name="add_role"),
    url(r'^add_staff/$', views.add_staff, name="add_staff"),
    url(r'^add_salary/$', views.add_salary, name="add_salary"),

    url(r'^edit_asset/$', views.edit_asset, name="edit_asset"),
    url(r'^edit_booking/$', views.edit_booking, name="edit_booking"),
    url(r'^edit_customer/$', views.edit_customer, name="edit_customer"),
    url(r'^edit_employee/$', views.edit_employee, name="edit_employee"),
    url(r'^edit_room/$', views.edit_room, name="edit_room"),
    url(r'^edit_staff/$', views.edit_staff, name="edit_staff"),
    url(r'^edit_salary/$', views.edit_salary, name="edit_salary"),
]