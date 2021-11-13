from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from post.models import Author
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import RegistrationForm, UserEditForm
from .tokens import account_activation_token

from allauth.account.views import SignupView

from .forms import MyLoginForm
# Create your views here.

def user_login(request):
    form = MyLoginForm()

    if request.method == "POST":
        login = form.cleaned_data['login']
        password = form.cleaned_data['password']
        remember_me = form.cleaned_data['remember']

        if form.is_valid():
            form.save()

            return redirect('home')
    else:
        form = MyLoginForm()

    context = {'form':form}

    return render(request, 'login.html', context)



def accounts_register(request):

    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password1'])
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activation de votre compte'
            message = render_to_string('registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject=subject, message=message)
            return HttpResponse('Compte créer avec succès, un lien d\'activation vous a été envoyé.')
    else:
        registerForm = RegistrationForm()
    return render(request, 'registration/register.html', {'form': registerForm})




def activate(request, uidb64, token, backend='django.contrib.auth.backends.ModelBackend'):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        messages.success(request, "Felicitations votre compte est actif.")
        return redirect('accounts:login')
    else:
        return render(request, 'registration/account_activation_invalid.html')


