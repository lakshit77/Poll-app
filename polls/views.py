from django.http import HttpResponse


def index(request):
    return HttpResponse("hello world. You are at poll index page")
