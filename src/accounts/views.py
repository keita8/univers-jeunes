from django.shortcuts import render, redirect
from .forms import UserForm
from django.views import generic
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import PasswordChangingForm, EditProfileForm
from post.models import Author 
# Create your views here.
def register(request):

	if request.user.is_authenticated:
		return redirect('home')

	if request.method == 'POST':

		form = UserForm(request.POST)

		if form.is_valid():
			form.save()
			messages.success(request, 'Votre compte a été crée avec succès')
			return redirect('accounts:login')
		else:
			return redirect('accounts:register')
	else:
		form = UserForm()


	template_name = "accounts/register.html"
	context = {'form':form}


	return render(request, template_name, context)



class PasswordsChangeView(PasswordChangeView):
	form_class = PasswordChangingForm
	success_url = reverse_lazy('accounts:password_success')


def password_success(request):

	template_name = 'registration/password_success.html'
	context = {}

	return render(request, template_name, context)


class UserEditView(generic.UpdateView):
	form_class = EditProfileForm
	template_name = 'registration/edit_profile.html'
	success_url = reverse_lazy('home')

	def get_object(self):
		return self.request.user



class ShowProfilePageView(generic.DetailView):
	model = Author
	template_name = 'registration/user_profile.html'

	def get_context_data(self, *args, **kwargs):
		pass