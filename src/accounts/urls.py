from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from .forms import LoginForm

app_name = 'accounts'

urlpatterns = [
	
	path('register/', register, name='register'),
	path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', redirect_authenticated_user=True, authentication_form=LoginForm), name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html', next_page='accounts:login'), name='logout'),
	path('password/', PasswordsChangeView.as_view(template_name='registration/password-change.html'), name='password-change'),
	path('password_success/', password_success, name='password_success'),
	path('edit_profile/', UserEditView.as_view(), name='edit_profile' ),
	path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile'),
]