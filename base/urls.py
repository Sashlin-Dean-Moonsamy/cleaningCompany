from django.urls import path
from . import views

app_name = 'base'
urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('bookings/', views.bookings, name="bookings"),
    path('logout/', views.logoutView, name='logoutView')
]
