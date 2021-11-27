from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
# from .models import CustomUser

class LoginForm(AuthenticationForm):
	username = forms.CharField(label='Nom d\'utilisateur' ,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"Nom d'utilisateur", 'required':'required'}))
	password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':"Mot de passe", 'required':'required'}))



class UserForm(UserCreationForm):

	class Meta:
		model = User
		fields = ('username', 'password1', 'password2')

	username = forms.CharField(label='Nom d\'utilisateur' ,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"Nom d'utilisateur", 'required':'required'}))
	password1 = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':"Mot de passe", 'required':'required'}))
	password2 = forms.CharField(label="Confirmer mot de passe", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':"Confirmer votre mot de passe", 'required':'required'}))


class PasswordChangingForm(PasswordChangeForm):
	old_password = forms.CharField(label='Ancien mot de passe' ,widget=forms.PasswordInput(attrs={'class':'form-control', 'type': 'password', 'placeholder':"Ancien mot de passe", 'required':'required'}))
	new_password1 = forms.CharField(label="Nouveau mot de passe", widget=forms.PasswordInput(attrs={'class':'form-control', 'type': 'password', 'placeholder':"Nouveau mot de passe", 'required':'required'}))
	new_password2 = forms.CharField(label="Confirmer nouveau mot de passe", widget=forms.PasswordInput(attrs={'class':'form-control', 'type': 'password', 'placeholder':"Confirmer votre nouveau mot de passe", 'required':'required'}))

	class Meta:
		model = User
		fields = ('old_password', 'new_password1', 'new_password2')



class EditProfileForm(UserChangeForm):
	email = forms.CharField(label='Email', max_length=200, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Adresse email', 'type':'email', 'required':'required'}))
	username = forms.CharField(label="Nom d'utilisateur", max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nom d\'utilisateur', 'type':'text', 'required':'required'}))
	first_name = forms.CharField(label='Prenom', max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Prenom', 'type':'text'}))
	last_name = forms.CharField(label='Nom', max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nom', 'type':'text'}))

	class Meta:
		model = User
		fields = ('username', 'last_name', 'first_name', 'email')
