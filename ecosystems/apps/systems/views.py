from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import logout
from .models import Accesses
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def log_in(request):
    if 'login' not in request.session:
        return render(request, "login.html", {})
    else:
        allAccesses = Accesses.objects.filter(owner=request.session['login'])
        users = User.objects.all()
        return render(request, "index.html", {'Accesses': allAccesses})


def addAccess(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        service = request.POST.get('service')
        login = request.POST.get('login')
        password = request.POST.get('password')
        comment = request.POST.get('comment')
        owner = request.POST.get('owner')

    if User.is_active:
        dataAccess = Accesses(title=title, service=service, login=login, password=password, comment=comment,
                              owner=request.session['login'])

    user = User.objects.create_user(username=login, password=password, first_name=owner)
    user.is_active = True
    user.save()
    dataAccess.save()
    return HttpResponseRedirect("/")


def changeAccess(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        title = request.POST.get('title')
        service = request.POST.get('service')
        login = request.POST.get('login')
        password = request.POST.get('password')
        comment = request.POST.get('comment')
        owner = request.POST.get('owner')
    Accesses.objects.filter(id=id).update(title=title, service=service, login=login, password=password, comment=comment,
                                          owner=owner)
    return HttpResponseRedirect("/")


def deleteAccess(request):
    if request.method == 'POST':
        id = request.POST.get('id')
    Accesses.objects.filter(id=id).delete()
    return HttpResponseRedirect("/")


def auth(request):
    username = request.POST.get('login')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
            request.session['login'] = username
            print("User is valid, active and authenticated")
        else:
            print("The password is valid, but the account has been disabled!")
    else:
        print("The username and password were incorrect.")
    return HttpResponseRedirect("/")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")
