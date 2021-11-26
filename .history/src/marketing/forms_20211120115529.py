from django import forms
from .models import Signup


class EmailSignupForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "type": "email",
        "name": "email",
        "id": "email",
        "placeholder": "Votre adresse Email",
    }), label="")

    class Meta:
        model = Signup
        fields = ('email', )
