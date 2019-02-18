from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import logout
from .models import Accesses
from passlib.hash import pbkdf2_sha256
from django.contrib.auth import authenticate, login


def index(request):
    allAccesses = Accesses.objects.all();
    return render(request, "index.html", {'Accesses': allAccesses})


def addAccess(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        service = request.POST.get('service')
        login = request.POST.get('login')
        password = request.POST.get('password')
        comment = request.POST.get('comment')
        owner = request.POST.get('owner')

    enc_password = pbkdf2_sha256.hash(password)

    if User.is_active:
        request.session['login'] = login
        dataAccess = Accesses(title=title, service=service, login=login, password=enc_password, comment=comment,
                              owner=request.session['login'])

    user = User.objects.create_user(username=login, password=password, first_name=owner)
    user.is_active = False
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
            print("User is valid, active and authenticated")
        else:
            print("The password is valid, but the account has been disabled!")
    else:
        print("The username and password were incorrect.")
    return HttpResponseRedirect("/")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")
