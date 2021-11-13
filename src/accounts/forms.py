from __future__ import absolute_import
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from allauth.account.forms import LoginForm, ResetPasswordForm, SignupForm, ChangePasswordForm
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, PasswordChangeForm, SetPasswordForm, UserCreationForm
from allauth.account.forms import AddEmailForm
import warnings
from importlib import import_module
from django import forms
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.core import exceptions, validators
from django.urls import reverse
from allauth.account.forms import SignupForm
from django import forms
from django.utils.translation import gettext, gettext_lazy as _, pgettext
from .utils import (
    build_absolute_uri,
    get_username_max_length,
    set_form_field_order,
)
# from . import app_settings
# from .adapter import get_adapter
# from .app_settings import AuthenticationMethod
# from .models import EmailAddress
# from .utils import (
#     filter_users_by_email,
#     get_user_model,
#     perform_login,
#     setup_user_email,
#     sync_user_email_addresses,
#     url_str_to_user_pk,
#     user_email,
#     user_pk_to_url_str,
#     user_username,
# )




# FORMULAIRE DE CONNECTION
# class MyLoginForm(LoginForm):
#     login = forms.CharField(label="Nom d'utilisateur", widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': "Nom d'utilisateur ici", "required": "true", "name": "username"}))
#     password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(
#         attrs={'class': 'form-control', 'placeholder': "Mot de passe", "required": "true", "name": "password"}))


# FORMULAIRE D'INSCRIPTION
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Nom d'utilisateur", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Nom d'utilisateur", "required": "true"}))
    email = forms.CharField(label="Email", widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': "Adresse Email", "required": "true"}))
    password1 = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': "Mot de passe", "required": "true"}))
    password2 = forms.CharField(label="Confirmer mot de passe", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': "Confirmer votre mot de passe", "required": "true"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

# FORMULIARE DE REINITIALISATION DU MOT DE PASSE
class PwdResetForm(PasswordResetForm):

    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control ', 'placeholder': 'Votre adresse email', 'id': 'form-email'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        test = User.objects.filter(email=email)
        if not test:
            raise forms.ValidationError(
                'Cette adresse email n\'est associée à aucun compte.')
        return email


# FORMULAIRE D'INSCRIPTION
class RegistrationForm(forms.ModelForm):
    
    username = forms.CharField(label="Nom d'utilisateur", min_length=3, max_length=50)
    email = forms.EmailField(max_length=100, error_messages={'required': 'Veuillez fournir une adresse email'})
    password1	 = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)
    password2    = forms.CharField( label='Confirmer mot de passe', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Ce nom d'utilisateur est déjà pris")
        return username

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Les mots de passe ne correspondent pas.')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Cette adresse email est déjà associée à un autre compte')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control ', 'placeholder': 'Nom d\'utilisateur'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control ', 'placeholder': 'Adresse email', 'name': 'email', 'id': 'id_email'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Mot de passe'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Confirmer votre mot de passe'})
        

# FORMULAIRE D'EDITION DU PROFIL
class UserEditForm(forms.ModelForm):
    
    first_name = forms.CharField(
        label='Firstname', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Firstname', 'id': 'form-firstname'}))

    last_name = forms.CharField(
        label='Lastname', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Lastname', 'id': 'form-lastname'}))

    email = forms.EmailField(
        max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Old Password', 'id': 'form-email'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Please use another Email, that is already taken')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['last_name'].required = False
        self.fields['email'].required = False


class PwdChangeForm(PasswordChangeForm):
    old_password  = forms.CharField(label='Ancien mot de passe', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Ancien mot de passe'}))
    new_password1 = forms.CharField(label='Nouveau mot de passe', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Nouveau mot de passe'}))
    new_password2 = forms.CharField(label='Confirmer votre mot de passe', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirmer votre mot de passe'}))




class PwdResetConfirmForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'] = forms.CharField(label='Nouveau mot de passe', widget=forms.PasswordInput(attrs={'class': 'form-control ', 'placeholder': 'Nouveau mot de passe', 'id': 'form-newpass'}))
        self.fields['password2'] = forms.CharField(label='Nouveau mot de passe', widget=forms.PasswordInput(attrs={'class': 'form-control ', 'placeholder': 'Confirmer nouveau mot de passe', 'id': 'form-newpass'}))


class MyLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':"Votre pseudo"})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Mot de passe'})


class MyCustomResetPasswordForm(ResetPasswordForm):

    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control ', 'placeholder': 'Votre adresse email', 'id': 'form-email'}))


    def save(self, *args, **kwargs):

        # Ensure you call the parent class's save.
        # .save() returns a string containing the email address supplied
        email = super(MyCustomResetPasswordForm, self).save(*args, **kwargs)

        # Add your own processing here.

        # Ensure you return the original result
        return email


class CustomSignupForm(SignupForm):
    username  = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"Pseudonyme", "required":"required", "id":"id_username"}))
    email     = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Adresse email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Mot de passe'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirmer votre mot de passe'}))


    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Cette adresse email est déjà prise')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError('Les mots de passe ne correspondent pas.')
        return password2


    def save(self, request):
        user           = super(CustomSignupForm, self).save(request)
        user.username  = self.cleaned_data['username']
        user.email     = self.cleaned_data['email']
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']
        user.save()
        return user





# class PasswordVerificationMixin(object):
#     def clean(self):
#         cleaned_data = super(PasswordVerificationMixin, self).clean()
#         password1 = cleaned_data.get("password1")
#         password2 = cleaned_data.get("password2")
#         if (password1 and password2) and password1 != password2:
#             self.add_error("password2", _("You must type the same password each time."))
#         return cleaned_data



class MyCustomChangePasswordForm(ChangePasswordForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomChangePasswordForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'



class MyCustomAddEmailForm(AddEmailForm):

    email = forms.EmailField(
        max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Ajouter un email', 'id': 'form-email'}))


class MySignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(MySignupForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


from allauth.account.forms import SetPasswordForm
class MyCustomSetPasswordForm(SetPasswordForm):

    def save(self):

        # Ensure you call the parent class's save.
        # .save() does not return anything
        super(MyCustomSetPasswordForm, self).save()

        # Add your own processing here.