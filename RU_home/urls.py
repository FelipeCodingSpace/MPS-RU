from django.urls import path
from . import views

urlpatterns = [
    path('cardapio/', views.ver_cardapio, name="ver_cardapio"),
    path('cadastro/', views.cadastrar_aluno, name="cadastrar_aluno"),
    path('login/', views.logar, name="logar"),
    path('inicio/', views.index, name="inicio")
]