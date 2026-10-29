from django.contrib import admin
from .models import Aluno, Curso


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
  list_display = ("nome", "sobrenome", "email")
  search_fields = ("nome", "sobrenome", "email")


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
  list_display = ("titulo", "descricao")
  search_fields = ("titulo",)
  filter_horizontal = ("alunos",)