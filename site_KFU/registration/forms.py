from django import forms
from .models import *


class MemberForm(forms.ModelForm):

  class Meta:
    model = Member
    fields = '__all__'
    exclude = ['login', 'password', 'organization']
    widgets = {
                'birthday': forms.SelectDateWidget(years=range(1999, 2017)),
                'issue_date': forms.SelectDateWidget(years=range(2013, 2021)),
              }


class WorkForm(forms.ModelForm):
  section = forms.ModelChoiceField(Section.objects.all(), label='Секция', required=True)
  class Meta:
    model = Work
    fields = '__all__'
    include = []
    exclude = ['review', 'organization', 'theses']


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