from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import Registeration, SignUp,SignIn
from .models import User
from django.contrib.auth import authenticate

# Create your views here.

# This function is for Sign Up.
def sign_in(request):
    if request.method == 'POST':
        em = request.POST.get('Email')
        pw = request.POST.get('Password')
        print(em,pw)
        user = User.objects.get(email=em, password=pw)
        print("Login User",user)
        if user is not None:
            stud = User.objects.all()
            return render(request,'addandshow.html', {'form':"", 'stu':stud})
    
            # print("if")
            # add_show(request)
            # return redirect('addandshow')
        else:
            print("else")
            return render(request, 'login.html')

        # try:
        #     user_registered=User.objects.all(email=em, password=pw)
        #     if len(user_registered)>0:
        #         print("In")
        #         return redirect('add_show')
        #     else:
        #         stat="Your Id or Password is invalid !"
        #         print("User is not registered")
        #         return render(request, 'signin.html',{'status':stat})
        # except:
        #     pass

    return render(request, 'login.html')


# This function is for Sign Up.
def sign_up(request):
    if request.method == 'POST':
        print("smit")
        nm = request.POST.get('Name')
        em = request.POST.get('Email')
        pw = request.POST.get('Password')
        reg = User(name=nm, email=em, password=pw)
        reg.save()
        fm = Registeration()
    else:
        fm = Registeration()    
    return render(request, 'signup.html')


# This function will Add & Show the data. 
def add_show(request):
    if request.method == 'POST':
        print("Hello")
        fm = Registeration(request.POST)
    #     if fm.is_valid():
    #         print("1")
    #         nm = fm.cleaned_data['name']
    #         em = fm.cleaned_data['email']
    #         pw = fm.cleaned_data['password']
    #         reg = User(name=nm, email=em, password=pw)
    #         reg.save()
    #         fm = Registeration()
    # else:
    #     print("2")
    #     fm = Registeration()
    stud = User.objects.all()

    return render(request,'addandshow.html', {'form':"", 'stu':stud})


# This function will Update(Edit) the data
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = Registeration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = Registeration(instance=pi)
    return render(request, 'updatest.html', {'form':fm})

# This function will Add & Show the data. 
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id) 
        pi.delete()
        return HttpResponseRedirect('/')