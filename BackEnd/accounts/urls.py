from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:username>/', views.profile),
    path('check-username/<str:username>/',views.check_username)
]