from django.shortcuts import render
from .models import Aluno, Curso

def home(request):
  return render(request, "escola/home.html")

def listar_alunos(request):
  alunos = Aluno.objects.all().order_by("nome", "sobrenome")

  return render(
      request,
      "escola/alunos.html",
      {"alunos": alunos}
  )


def listar_cursos(request):
  cursos = Curso.objects.prefetch_related("alunos").all().order_by("titulo")

  return render(
      request,
      "escola/cursos.html",
      {"cursos": cursos}
  )