from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.
def home(req):
    return render(req,'home.html',)
def about(req):
    return render(req,'about.html',)
def contact(req):
    if req.method=='POST':
        form=contact_form(req.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']
            data=Contact.objects.create(name=name,email=email,message=message)
            data.save()
            return redirect(contact)
    form=contact_form()
    return render(req,'contact.html')
def course(req):
    if req.method=='POST':
        form=course_form(req.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            phone=form.cleaned_data['phone']
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']
            coursee=form.cleaned_data['coursee']
            data=Students.objects.create(name=name,phone=phone,email=email,message=message,coursee=coursee)
            data.save()
            return redirect(course)
    form=course_form()
    return render(req,'course.html',{'form':form})

