from django.urls import path
from . import views

urlpatterns = [
    path('', views.exchange),
    path('store/', views.store),
    path('search/<str:nation>', views.search),
]
