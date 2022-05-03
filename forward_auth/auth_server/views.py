from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect

from .utils import (
    get_redirect_uri,
    get_public_uri,
    is_authenticated,
)


def auth(request: HttpRequest):
    redirect_uri = get_redirect_uri(request)
    if is_authenticated(request):
        return HttpResponse("OK")
    elif not redirect_uri:
        return redirect(f"{get_public_uri()}/auth/login/")
    return HttpResponse("Unauthorized", status=401)


def signin(request: HttpRequest):
    redirect_uri = get_redirect_uri(request)
    if request.user.is_authenticated:
        return redirect(redirect_uri)
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response: HttpResponse = redirect(redirect_uri)
            return response
        else:
            return HttpResponse("Invalid login")
    return render(request, "login.html")


def signout(request: HttpRequest):
    if request.user.is_authenticated:
        logout(request)
        redirect_uri = get_redirect_uri(request, default="/")
        return redirect(redirect_uri)
    else:
        return HttpResponse("You are not logged in")
