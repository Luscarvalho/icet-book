from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Emprestimo, Livro
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy


class MyEmprestimolistview(LoginRequiredMixin, ListView):
    model = Emprestimo
    template_name = 'emprestimo/meus.html'
    context_object_name = 'emprestimos'

    def get_queryset(self):
        return Emprestimo.objects.filter(borrower=self.request.user)


class Emprestimolistview(LoginRequiredMixin, ListView):
    model = Emprestimo
    template_name = 'emprestimo/solicitados.html'
    context_object_name = 'emprestimos'

    def get_queryset(self):
        return Emprestimo.objects.filter(lender=self.request.user)


class LivrosDetailView(LoginRequiredMixin, DetailView):
    model = Livro
    template_name = 'books/detalhe.html'


@login_required
def emprestar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)

    emprestimo_existente = Emprestimo.objects.filter(
        borrower=request.user, book=livro).exists()

    if emprestimo_existente:
        messages.error(request, 'Você já solicitou empréstimo desse livro antes.')
        return redirect('home')
    else:
        Emprestimo.objects.create(
            borrower=request.user, lender=livro.usuario, book=livro, status='pending')
        messages.success(request, 'Empréstimo criado com sucesso.')

    return redirect('meus-emprestimo')


@login_required
def aceitar_emprestimo(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, pk=emprestimo_id)

    if (request.user == emprestimo.lender and emprestimo.status == 'pending' or request.user == emprestimo.lender
            and emprestimo.status == 'denied'):
        emprestimo.status = 'approved'
        emprestimo.save()

        emprestimo.book.status = 'indisp'
        emprestimo.book.save()

    return redirect('emprestimo')


@login_required
def recusar_emprestimo(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, pk=emprestimo_id)

    if (request.user == emprestimo.lender and emprestimo.status == 'pending' or request.user == emprestimo.lender
            and emprestimo.status == 'approved'):
        emprestimo.status = 'denied'
        emprestimo.save()

        emprestimo.book.status = 'disp'
        emprestimo.book.save()

    return redirect('emprestimo')


class DeleteEmprestimo(LoginRequiredMixin, DeleteView):
    model = Emprestimo
    template_name = 'emprestimo/delete.html'
    success_url = reverse_lazy('meus-emprestimo')

    def test_func(self):
        book = self.get_object()
        if self.request.user == book.usuario:
            return True
        else:
            messages.error(
                self.request, 'Você não tem permissão para excluir este empréstimo.')
            return False

    def handle_no_permission(self):
        return redirect('meus-emprestimo')


@login_required
def devolver_emprestimo(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, pk=emprestimo_id)

    if (request.user == emprestimo.borrower
            and emprestimo.status == 'approved'):

        emprestimo.book.status = 'devol'
        emprestimo.book.save()

    return redirect('meus-emprestimo')


@login_required
def aceitar_devolucao(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, pk=emprestimo_id)

    if (request.user == emprestimo.lender
            and emprestimo.book.status == 'devol'):
        emprestimo.status = 'concluded'
        emprestimo.save()

        emprestimo.book.status = 'disp'
        emprestimo.book.save()

    return redirect('emprestimo')