from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

def home(request):
	return render(request, 'working/index.html')

def about(request):
	return render(request, 'working/about.html') 

def services(request):
	return render(request, 'working/service.html')

def contactnifo(request):
	return render(request, 'working/contact-us.html')

def showPost(request):
	na = request.POST.get(name1)
	em = request.POST.get(email1)
	sub = request.POST.get(subject1)
	mess = request.POST.get(message1)

	o_ref = Post(name=na, email=em, subject1=sub, message=mess)
	o_ref.save()

	return None