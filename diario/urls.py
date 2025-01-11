from django.urls import path
from . import views
urlpatterns = [  
  path('', views.home),
  path('escrever/', views.escrever, name='escrever'),
  path('cadastrar_pessoa/', views.cadastrar_pessoa, name='cadastrar_pessoa')
]
