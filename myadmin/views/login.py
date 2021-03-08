from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from myadmin.forms import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login

def admin_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],
                                      password=cd['password'])
            if user is not None:
                if user.is_active and user.is_staff:
                    login(request,user)
                    return redirect("dashboard_admin")
                else:
                    messages.error(request, "Disabled Account!")
                    return redirect("adminLogin")
            else:
                messages.error(request, "Invalid login!")
                return redirect("adminLogin")
    else:
        form=LoginForm()
    return render(request,'myadmin/login.html',{'form':form})

def logout(request):
    request.session.clear()
    return redirect('adminLogin')