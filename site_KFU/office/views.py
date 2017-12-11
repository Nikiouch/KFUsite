from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Достать юзера по ID, рендер шаблона с кнопками
# Переделать if`ы на проверку списков/словарей

def office(request, ID):
	ThisMember = Member.objects.get(id=ID)
	if request.method == "POST":
		if "Work" in request.POST:
			return redirect("work", ID=ID)
		if "Organization" in request.POST:
			return redirect("organization", ID=ID)
		if "Member" in request.POST:
			return redirect("member", ID=ID)
		if "Director" in request.POST:
			return redirect("director", ID=ID)
		if "Receipt" in request.POST:
			return redirect("receipt", ID=ID)
	return render(request, "office.html", {"MemberName": ThisMember.get_full_name(), "ID": ID, })

def work(request, ID):
	ThisMember = Member.objects.get(id=ID)
	ThisWork = DirectorMember.objects.get(member=ThisMember.pk).work
	if request.method == "POST":
		ThisWorkForm = WorkForm(request.POST, instance=ThisWork)
		if "Next" or "Change" in request.POST:
			if ThisWorkForm.has_changed() and ThisWorkForm.is_valid():
				for i in range(ThisWorkForm.changed_data.__len__()):
					ThisWork.i = ThisWorkForm.changed_data[i]
				print("PRE-SAVE")
				ThisWork.save(update_fields=["name"])
			if "Next" in request.POST:
				return redirect("member", ID=ThisMember.pk)
			else:	# CHANGE
				return render(request, "office.html", {"MemberName": ThisMember.get_full_name(), "form": WorkForm(instance=ThisWork), "ID": ID})
	return render(request, "office.html", {"MemberName": ThisMember.get_full_name(), "form": WorkForm(instance=ThisWork), "ID": ID})

def member(request, ID):
	ThisMember = Member.objects.get(id=ID)
	if request.method == "POST":
		ThisMemberForm = MemberForm(request.POST, instance=ThisMember)
		if ThisMemberForm.has_changed() and ThisMemberForm.is_valid():
			for i in range(ThisMemberForm.changed_data.__len__()):
				ThisMember.i = ThisMemberForm.changed_data[i]
			ThisMember.save(update_fields=None)
		if "Change" in request.POST:
			return render(request, "office.html", {"MemberName": ThisMember.get_full_name(), "form": MemberForm(instance=ThisMember), "ID": ID})
		if "Next" in request.POST:
			return redirect("director", ID=ThisMember.pk)
	return render(request, "office.html", {"MemberName": ThisMember.get_full_name(), "form":MemberForm(instance=ThisMember), "ID": ID})

def director(request, ID):
	ThisMember = Member.objects.get(id=ID)
	ThisDirector = DirectorMember.objects.get(member=ThisMember.pk).director
	if request.method == "POST":
		ThisDirectorForm = DirectorForm(request.POST, instance=ThisDirector)
		if ThisDirectorForm.has_changed() and ThisDirectorForm.is_valid():
			for i in range(ThisDirectorForm.changed_data.__len__()):
				ThisDirector.i = ThisDirectorForm.changed_data[i]
			ThisDirector.save(update_fields=None)
		if "Change" in request.POST:
			return render(request, "office.html", {"MemberName": ThisMember.get_full_name(), "form":DirectorForm(instance=ThisDirector), "ID": ID})
		else:
			return redirect("organization", ID=ThisMember.pk)
	return render(request, "office.html", {"MemberName": ThisMember.get_full_name(), "ID": ID})

def organization(request, ID):
	ThisMember = Member.objects.get(id=ID)

	return render(request, "office.html", {"MemberName": ThisMember.get_full_name(), "ID": ID})

def receipt(request, ID):
	ThisMember = Member.objects.get(id=ID)

	return render(request, "office.html", {"MemberName": ThisMember.get_full_name(), "ID": ID})