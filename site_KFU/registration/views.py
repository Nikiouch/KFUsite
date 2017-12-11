from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
#from django.template.context_processors import csrf
#from django.template import context
from .forms import *
from .models import *
from .functions import eng_translate, GeneratePassword

# WORK_ORG_MEMBER_DIRECTOR_DOCUMENTS

# !!! ЛОГИН - СКОРАЩЕНИЕ ФИО+ID !!!

def work_registration(request):
	#cont = {}
	#request.session.set_expiry(3600)
	title = 'Научная работа'
	#cont['title'] = title
	#cont['form'] = WorkForm
	# print('WRK:' + ' ' + request.session.get('work_section') + ' ' + request.session.get('work_name'))
	if request.method == "POST":
		print('POST')
		work_form = WorkForm(request.POST, auto_id=True)#, request.FILES)
		if work_form.is_valid():
			work_form = WorkForm(request.POST).save()
			#request.session['work_name'] = work_form.cleaned_data['name']
			#request.session['section_id'] = work_form['section'].value()
			#cont['form'] = OrganizationForm
			#print(request.session['work_name'] + ' ' + request.session['section_id'])
			return redirect('org_registration', workid=work_form.pk)
		else:
			return render(request, "registration.html", {'form': WorkForm, 'title': title})
	else:
		return render(request, "registration.html", {'form': WorkForm, 'title': title})


def org_registration(request, workid):
	#cont2 = {}
	title = 'Направляющая организация'
	#cont2['form'] = OrganizationForm
	#cont2['title'] = title
	#cont2.update(csrf(request))
	#print("ORG:"+' '+request.session.get('work_name')+' '+request.session.get('section_id'))
	if request.method == "POST":
		org_form = OrganizationForm(request.POST, auto_id=True)
		if org_form.is_valid():
			new_org = OrganizationForm(request.POST, auto_id=True).save()

			return redirect('member_registration', directormemberID=1, orgID=1)
		else:
			return render(request, "registration.html", {'form': OrganizationForm, 'title': title})
	else:
		return render(request, "registration.html", {'form': OrganizationForm, 'title': title})


# НАЙТИ DIRECTORMEMBER, ДОБАВИТЬ УЧАСТНИКА
def member_registration(request, directormemberID, orgID):
	title = 'Участник'
	member_form = MemberForm(request.POST, auto_id=True)
	if request.method == "POST":
		DirectorMember_ByWork = DirectorMember.objects.get(id=directormemberID)
		#print(DirectorMember_ByWork)
		if member_form.is_valid():
			new_member = Member()
			new_member.organization = Organization.objects.get(pk=orgID)
			new_member = member_form.save()
			DirectorMember_ByWork.member = new_member
			DirectorMember_ByWork.save()
			return redirect('director_registration', directormemberID=directormemberID)
		else:
			return render(request, "registration.html", {'form': MemberForm, 'title': title})
	return render(request, "registration.html", {'form': MemberForm, 'title': title})


# НАЙТИ DIRECTORMEMBER, ДОБАВИТЬ НАУЧРУКА
def director_registration(request, directormemberID):
	title = 'Научный руководитель'
	director_form = DirectorForm(request.POST, auto_id=True)
	if request.method == "POST":
		DirectorMember_ByID = DirectorMember.objects.get(id=directormemberID)
		if director_form.is_valid():
			NewDirector =	director_form.save()

			DirectorMember_ByID.director = NewDirector
			return redirect('finale')
		else:
			return render(request, "registration.html", {'form': director_form, 'title': title})
	return render(request, "registration.html", {'form': director_form, 'title': title})


# DOCUMENTS
# ДОБАВИТЬ ДОКУМЕНТЫ
def finale(request):
	application_form = DocumentsForm(request.POST, auto_id=True)
	title = 'Завершение регистрации'
	if request.method == "POST":
		if application_form.is_valid():
			NewDocs = Documents()
			NewDocs = application_form.save()
			return redirect("/login")
		else:
			return render(request, "registration.html", {'form': application_form, 'title': title})
	else:
		return render(request, "registration.html", {'form': application_form, 'title': title})
