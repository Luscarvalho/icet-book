from django.urls import path
from livro import views

urlpatterns = [
    path('', views.LivrosListView.as_view(), name='home'),
    path('livros/meus/', views.MyLivrosListView.as_view(), name='my-livros-list'),
    path('livros/cadastrar/', views.LivrosCreateView.as_view(), name='livros-create'),
    path('livros/editar/<int:pk>/',
         views.LivrosUpdateView.as_view(), name='livros-update'),
    path('livros/apagar/<int:pk>/',
         views.LivrosDeleteView.as_view(), name='livros-delete'),
]
