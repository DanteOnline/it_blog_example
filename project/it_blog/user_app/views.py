from django.shortcuts import render, HttpResponseRedirect, Http404
from django.contrib import auth
from .forms import MyRegistrationForm


def login(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect("/")
        else:
            return render(request, 'login.html', {'username': username, 'errors': True})
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/user/login/')


def registration(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/user/login/')
        context = {'form': form}
        return render(request, 'registration.html', context)
    context = {'form': MyRegistrationForm()}
    return render(request, 'registration.html', context)

