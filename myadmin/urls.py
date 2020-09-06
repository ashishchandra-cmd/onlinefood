from django.urls import path
from myadmin import  views

urlpatterns = [
    path('',views.myadmin_login_page),
    path('myadmin_login/',views.myadmin_login,name='myadmin_login'),
    path('admin_home/',views.admin_home,name='admin_home'),
    path('state_create/',views.state_create,name='state_create'),
    path('state_details/',views.state_details,name='state_details'),
    path('state_delete(?P<int:id>)/',views.state_delete,name='state_delete'),
    path('state_update(?P<int:id>)/',views.state_update, name='state_update'),

    path('city_create/',views.city_create, name='city_create'),
    path('city_details/',views.city_details,name='city_details'),
    path('city_delete(?P<int:id>)/',views.city_delete,name='city_delete'),
    path('city_update(?P<int:id>)/',views.city_update, name='city_update'),

    path('cuisine_create/',views.cuisine_create, name='cuisine_create'),
    path('cuisine_details/',views.cuisine_details,name='cuisine_details'),
    path('cuisine_delete(?P<int:id>)/',views.cuisine_delete,name='cuisine_delete'),
    path('cuisine_update(?P<int:id>)/',views.cuisine_update, name='cuisine_update'),
]
