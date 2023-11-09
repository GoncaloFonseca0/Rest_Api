from django.urls import re_path as url, include
from django.urls import path, re_path
from EmployeeApp import views
from django.conf.urls.static import static


urlpatterns = [

    re_path (r'^Contract$',views.ContractApi),
    re_path (r'^Contract$', views.ContractApi),
    re_path(r'^Contract/([0-9]+)$',views.ContractApi),
    re_path (r'^Client$',views.ClientApi),
    re_path (r'^Client$', views.ClientApi),
    re_path(r'^Client/([0-9]+)$',views.ClientApi),
    re_path(r'^Contract_clientApi$',views.Contract_clientApi),

    #path('Contract/', views.ContractApi),
    #path('Client/', views.ClientApi),
    #re_path(r'^client$',views.ClientApi),
    #path('client/<int:id>/', views.ClientApi),
   
    

]
