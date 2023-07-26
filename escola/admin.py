from django.contrib import admin
from escola.models import Aluno, Curso, Matricula

class Alunos(admin.ModelAdmin):
    # Campos para exibir no admin
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    # Campos que deixa clicar quando altera
    list_display_links = ('id', 'nome')
    # Buscar alunos
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
    # Campos para exibir no admin
    list_display = ('id', 'codigo_curso', 'descricao')
    # Campos que deixa clicar quando altera
    list_display_links = ('id', 'codigo_curso')
    # Buscar alunos
    search_fields = ('codigo_curso',)
    list_per_page = 20

admin.site.register(Curso, Cursos)

class Matriculas(admin.ModelAdmin):
    # Campos para exibir no admin
    list_display = ('id', 'aluno', 'curso')
    # Campos que deixa clicar quando altera
    list_display_links = ('id', )

admin.site.register(Matricula, Matriculas)
