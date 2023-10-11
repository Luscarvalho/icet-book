from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Livro


class LivrosListView(LoginRequiredMixin, ListView):
    model = Livro
    template_name = 'home.html'
    context_object_name = 'filme'

    def get_queryset(self):
        return Livro.objects.exclude(Q(usuario=self.request.user) | Q(status='indisp'))


class MyLivrosListView(LoginRequiredMixin, ListView):
    model = Livro
    template_name = 'books/mybooks.html'

    def get_queryset(self):
        return Livro.objects.filter(usuario=self.request.user)


class LivrosCreateView(LoginRequiredMixin, CreateView):
    model = Livro
    template_name = 'books/form.html'
    fields = ['nome', 'autor']
    success_url = reverse_lazy('my-livros-list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Cadastrar"
        context['botao'] = "Cadastrar"
        return context


class LivrosUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Livro
    template_name = 'books/form.html'
    fields = ['nome', 'autor']
    success_url = reverse_lazy('my-livros-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Editar"
        context['botao'] = "Editar"
        return context

    def test_func(self):
        book = self.get_object()
        if self.request.user == book.usuario:
            return True
        else:
            messages.error(
                self.request, 'Você não tem permissão para editar este filme.')
            return False

    def handle_no_permission(self):
        return redirect('my-livros-list')


class LivrosDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Livro
    template_name = 'books/delete.html'
    success_url = reverse_lazy('my-livros-list')

    def test_func(self):
        book = self.get_object()
        if self.request.user == book.usuario:
            return True
        else:
            messages.error(
                self.request, 'Você não tem permissão para excluir este filme.')
            return False

    def handle_no_permission(self):
        return redirect('my-livros-list')
