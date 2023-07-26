from rest_framework import viewsets
from escola.models import Aluno, Curso
from escola.serializer import AlunoSerializer, CursoSerializer

class AlunosViewSets(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""

    queryset = Aluno.objects.all();
    serializer_class = AlunoSerializer

class CursosViewSets(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""

    queryset = Curso.objects.all();
    serializer_class = CursoSerializer