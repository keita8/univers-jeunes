from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from .forms import PwdResetForm, PwdChangeForm, PwdResetForm, PwdResetConfirmForm, LoginForm
from allauth.account.views import LoginView

app_name = 'accounts'

urlpatterns = [
    
	# path('register/', accounts_register, name='register'),
	# path('login/', auth_views.LoginView.as_view(template_name='registration/login.html', redirect_authenticated_user=True, authentication_form=LoginForm), name='login'),
    # path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
	# path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html', next_page='accounts:login'), name='logout'),
	# path('password_reset/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html",form_class=PwdResetForm), name='password_reset'),
    # path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html', form_class=PwdResetConfirmForm), name="password_reset_confirm"),
    # path('profile/', views.profile, name='profile'),
    # path('profile/edit/', views.edit, name='edit'),
    # path('profile/delete/', views.delete_user, name='deleteuser'),
    # path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
    # path('password_change/', auth_views.PasswordChangeView.as_view(template_name="registration/password_change_form.html",form_class=PwdChangeForm), name='password_change'),
    # path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done')
]