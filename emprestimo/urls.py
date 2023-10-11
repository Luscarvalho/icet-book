from django.urls import path
from emprestimo import views

urlpatterns = [
    path('emprestimo/meus', views.MyEmprestimolistview.as_view(), name="meus-emprestimo"),
    path('emprestimo/solicitados', views.Emprestimolistview.as_view(), name="emprestimo"),
    path('livros/<int:pk>/', views.LivrosDetailView.as_view(),
         name='livros-detail'),
    path('livros/<int:pk>/emprestar/',
         views.emprestar_livro, name='emprestar_livro'),
    path('emprestimo/aceitar/<int:emprestimo_id>/',
         views.aceitar_emprestimo, name='aceitar-emprestimo'),
    path('emprestimo/recusar/<int:emprestimo_id>/',
         views.recusar_emprestimo, name='recusar-emprestimo'),
    path('emprestimo/apagar/<int:pk>/',
         views.DeleteEmprestimo.as_view(), name='deletar-emprestimo'),
    path('emprestimo/devolver/<int:emprestimo_id>/',
         views.devolver_emprestimo, name='devolver-emprestimo'),
    path('emprestimo/devolver/aceitar/<int:emprestimo_id>/',
         views.aceitar_devolucao, name='aceitar-devolucao'),
]
