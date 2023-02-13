
from . import views
from django.urls import path



app_name = 'accounts'

urlpatterns = [
    path('', views.login,name='login'),
    path('dashboard/', views.index,name='dashboard'),
    path('logout/', views.logout,name='logout'),
   
]
