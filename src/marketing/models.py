from django.db import models

# Create your models here.
class SignUp(models.Model):
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Date d'envoi")

	class Meta:
		verbose_name = 'Marketing'
		verbose_name_plural = 'Marketings'

	def __str__(self):
		return f'{self.email} '