from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class CustomAuthPermissionMixin:
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class AlunosViewSets(CustomAuthPermissionMixin, viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""

    queryset = Aluno.objects.all();
    serializer_class = AlunoSerializer

class CursosViewSets(CustomAuthPermissionMixin, viewsets.ModelViewSet):
    """Exibindo todos os cursos"""

    queryset = Curso.objects.all();
    serializer_class = CursoSerializer

class MatriculasViewSets(CustomAuthPermissionMixin, viewsets.ModelViewSet):
    """Exibindo todas as Matriculas"""

    queryset = Matricula.objects.all();
    serializer_class = MatriculaSerializer

class ListaMatriculasAlunoViewSets(CustomAuthPermissionMixin, generics.ListAPIView):
    """Lista todas as Matriculas do Aluno"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk']);
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer

class ListaAlunosMatriculadosViewSets(CustomAuthPermissionMixin, generics.ListAPIView):
    """Lista todos alunos matriculados em um curso"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer