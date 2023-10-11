from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from aluno.models import User
from django import forms
from django.core.exceptions import ValidationError


class CustomLoginForm(AuthenticationForm):
    error_messages = {
        "invalid_login": "Usuário ou senha incorretos."
    }


class CadastroForm(UserCreationForm):

    first_name = forms.CharField(label='Nome', max_length=30, required=True)
    last_name = forms.CharField(
        label='Sobrenome', max_length=30, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'matricula', 'curso', 'password1', 'password2']
        help_texts = {
            'username': None,
        }

    def clean_matricula(self):
        matricula = self.cleaned_data['matricula']
        if not matricula.isdigit():
            raise ValidationError('A matrícula deve conter apenas números.')
        return matricula

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
