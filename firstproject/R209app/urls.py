from django.urls import path
from . import views

urlpatterns = [
    path("affiche/<int:id>/", views.affiche),
    path('index/', views.index),
    path('ajout/', views.ajout),
    path('traitement/',views.traitement),
    path("update/<int:id>/",views.update),
    path("updatetraitement/<int:id>/", views.updatetraitement),
    path("delete/<int:id>/", views.delete),
]