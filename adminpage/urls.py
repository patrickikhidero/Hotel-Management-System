from django.conf.urls import url
from adminpage import views

urlpatterns = [
    url(r'^$', views.adminlogin, name="adminlogin"),
    url(r'^adminregister/$', views.adminregister, name="adminregister"),
    url(r'^logout/$', views.logoutPage, name = "logout"),
    url(r'^adminhome/$', views.adminhome, name="adminhome"),
    url(r'^add_asset/$', views.add_asset, name="add_asset"),

    url(r'^all_booking/$', views.all_booking, name="all_booking"),
    url(r'^all_customer/$', views.all_customer, name="all_customer"),
    url(r'^all_rooms/$', views.all_rooms, name="all_rooms"),
    url(r'^all_staff/$', views.all_staff, name="all_staff"),

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
    
    url(r'^profile/$', views.profile, name="profile"),
    url(r'^settings/$', views.settings, name="settings"),
    url(r'^logoutPage/$', views.logoutPage, name = "logoutPage"),
]