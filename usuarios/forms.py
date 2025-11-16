from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Formulario para iniciar sesión con correo electrónico
class EmailLoginForm(forms.Form):
    email = forms.EmailField(label="Correo electrónico")
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise forms.ValidationError("No existe un usuario con ese correo.")

        user = authenticate(username=user.username, password=password)
        if not user:
            raise forms.ValidationError("Correo o contraseña incorrectos.")

        self.cleaned_data['user'] = user
        return self.cleaned_data

# Formulario para crear cuenta con correo electrónico y sin textos de ayuda en inglés
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Correo electrónico", required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        labels = {
            "username": "Nombre de usuario",
            "password1": "Contraseña",
            "password2": "Confirmar contraseña",
        }
        help_texts = {
            "username": "",
            "password1": "",
            "password2": "",
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("El correo es obligatorio.")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo ya está registrado.")
        return email
