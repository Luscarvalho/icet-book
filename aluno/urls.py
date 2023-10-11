from django.contrib.auth import views as auth_views
from django.urls import path
from aluno import views
from .forms import CustomLoginForm

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='auth/login.html',
        authentication_form=CustomLoginForm
    ), name="login"),
    path('cadastro/', views.CadastroView.as_view(), name='cadastro'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
]
