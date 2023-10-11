from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    CURSOS = [
        ('ADS', 'Análise e Desenvolvimento de Sistemas'),
        ('SI', 'Sistemas para Internet'),
        ('BD', 'Banco de Dados'),
        ('GTI', 'Gestão da Tecnologia da Informação'),
    ]
    matricula = models.CharField(
        max_length=10, unique=True, verbose_name='Matrícula')
    curso = models.CharField(
        max_length=3, choices=CURSOS, verbose_name='Curso', default='ADS')
