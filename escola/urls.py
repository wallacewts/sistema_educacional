from django.urls import path
from . import views

urlpatterns = [
  path("", views.home, name="home"),
  path("alunos/", views.listar_alunos, name="listar_alunos"),
  path("cursos/", views.listar_cursos, name="listar_cursos"),
]