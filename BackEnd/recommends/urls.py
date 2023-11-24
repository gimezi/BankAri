from django.urls import path
from . import views

urlpatterns = [
    path('recomproducts/', views.save_recommendation),
]
