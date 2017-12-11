from django.shortcuts import render, redirect
# from django.http import QueryDict
from .models import *
from .forms import *

# ОТРИСОВКА ФОРМЫ ДЛЯ ВХОДА, РЕДИРЕКТ СЮДА С ГЛАВНОЙ СТРАНИЦЫ
def log_in(request):
	if request.method == "POST":
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			if "log_in" in request.POST:
				try:
					member = Member.objects.get(login=login_form.cleaned_data["login"], password=login_form.cleaned_data["password"])
				except:
					member = None
				if member is not None:
					return redirect('office', ID=member.pk)
			if "jury_log_in" in request.POST:
				try:
					jury = Jury.objects.get(login=login_form.cleaned_data["login"], password=login_form.cleaned_data["password"])
				except:
					jury = None
				if jury is not None:
					return redirect('jury', ID=jury.pk)
		else:
			return render(request, 'login.html', {'login_form': login_form}) # !!! + СООБЩЕНИЕ ОБ ОШИБКЕ
		# if Member.objects.filter()
	return render(request, 'login.html', {'login_form': LoginForm()})


# ЛИЧНЫЙ КАБИНЕТ
def office(request, memID):
		LoggedMemberWork = DirectorMember.objects.get(member=memID).work
		# print(LoggedMemberWork.__str__()+"___")
		if request.method == "POST":
			OfficeWorkForm = WorkForm(request.POST, instance=LoggedMemberWork)
			# Если нажата ИЗМЕНИТЬ
			if "Change" in request.POST:
				if OfficeWorkForm.has_changed() and OfficeWorkForm.is_valid():
					for i in range(OfficeWorkForm.changed_data.__len__()):
						LoggedMemberWork.i = OfficeWorkForm.changed_data[i]
					# print(LoggedMemberWork.__str__())
					LoggedMemberWork.save(update_fields=["name"])
					return render(request, 'office.html', {'form': OfficeWorkForm})
			elif "Next" in request.POST:
				# Если какой-то "гений" не нажал ИЗМЕНИТЬ, но изменил данные и пошел дальше
				if OfficeWorkForm.has_changed() and OfficeWorkForm.is_valid():
					for i in range(OfficeWorkForm.changed_data.__len__()):
						LoggedMemberWork.i = OfficeWorkForm.changed_data[i]
					LoggedMemberWork.save(update_fields=["name"])
		else:
			OfficeWorkForm = WorkForm(instance=LoggedMemberWork)
			return render(request, 'office.html', {'form': OfficeWorkForm})
		#return render(request, 'login.html', {'login_form': LoginForm})