from django.db import models
from aluno.models import User
from livro.models import Livro


class Emprestimo(models.Model):
    lender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='lender_requests')
    borrower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='borrower_requests')
    book = models.ForeignKey(Livro, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[(
        'pending', 'Pendente'), ('approved', 'Aprovado'), ('denied', 'Negado'), ('concluded', 'Concluído')])

    def __str__(self):
        return self.book.nome + ' - ' + self.book.autor + ' - ' + self.borrower.username
