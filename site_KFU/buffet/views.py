from django.shortcuts import render, redirect

def registration(request):
	print("BUFFET VIEW REDIRECT")
	return render(request, "login.html")