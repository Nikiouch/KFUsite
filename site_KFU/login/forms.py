from django import forms
from login.models import *


class LoginForm(forms.ModelForm):

	class Meta:
		model = Member
		fields = ["login", "password"]
		widgets = {
								"password": forms.PasswordInput(),
							}

class WorkForm(forms.ModelForm):

	class Meta:
		model = Work
		fields = "__all__"
		exclude = ["organization", "review", "theses"]

class DirectorForm(forms.ModelForm):

	class Meta:
		model = Director
		fields = '__all__'
		exclude = ['']


class OrganizationForm(forms.ModelForm):

	class Meta:
		model = Organization
		fields = '__all__'
		exclude = ['']


class DocumentsForm(forms.ModelForm):
	agreement = forms.BooleanField(required=True, label='Даю согласие на обработку личных данных')
	class Meta:
		model = Documents
		fields = '__all__'
		exclude = ['member', 'members_sertificate', 'directors_sertificate', 'receipt']