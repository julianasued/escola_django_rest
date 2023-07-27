from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSets, CursosViewSets, MatriculasViewSets, ListaMatriculasAlunoViewSets, ListaAlunosMatriculadosViewSets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSets, basename='Alunos')
router.register('cursos', CursosViewSets, basename='Cursos')
router.register('matriculas', MatriculasViewSets, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('alunos/<int:pk>/matriculas/', ListaMatriculasAlunoViewSets.as_view()),
    path('cursos/<int:pk>/matriculas/', ListaAlunosMatriculadosViewSets.as_view())
]
