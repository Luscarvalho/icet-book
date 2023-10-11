from django.db import models
from aluno.models import User


class Livro(models.Model):
    OPTIONS = [
        ('disp', 'Disponível'),
        ('indisp', 'Emprestado'),
        ('devol', 'Devolvido'),
    ]
    nome = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=OPTIONS, default='disp')
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome
