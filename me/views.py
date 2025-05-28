from django.shortcuts import render,redirect
from .models import Social_media, Contact_Me, Form, About_language, About_Me

def home(request):
    #Form
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        body = request.POST.get('body')
        
        if name and email and body:
            Form.objects.create(Name = name, Email = email, Body = body)
            return redirect('/')

    
    #socialmedia
    socialmedia = Social_media.objects.all().last()
    #Contact_Me
    contact = Contact_Me.objects.all().last()
    #About_language
    Aboutlan = About_language.objects.all().last()
    #about_me
    about_me = About_Me.objects.all().last()


    return render(request, "index.html", context={'socialmedia':socialmedia, 'contact':contact, 'language':Aboutlan, 'about':about_me})
