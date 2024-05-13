from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Contact

# Create your views here.
def deshboard (request):
    return render(request, 'index.html')
def home (request):
    return render(request, 'index.html')
def blog (request):
    return render(request, 'blog.html')
def about (request):
    return render(request, 'about.html')
def contact (request):
    if request.method=="POST":
       name = request.POST['name']
       email = request.POST['email']
       description = request.POST['description']
       values = Contact(name=name, email=email, description=description)
       values.save()
    return render(request, 'contact.html')