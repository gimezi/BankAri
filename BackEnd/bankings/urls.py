from django.urls import path
from . import views

urlpatterns = [
    path('1/', views.save_depositlist),
    path('2/', views.save_savinglist),
    path('3/', views.save_rentalloanlist),
    path('',views.get_bankings),
    path('deposit-detail/<str:id>/', views.deposit_detail),
    path('saving-detail/<str:id>/', views.saving_detail),
    path('rentalloan-detail/<str:id>/', views.rentalloan_detail),
]
