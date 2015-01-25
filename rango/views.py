from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hello world!<br />"
                        "<a href='/rango/about/'>About</a>")


def about(request):
    return HttpResponse("This tutorial has been put together by "
                        "<b>Adrian Musat</b>, <b>2088959m</b>.<br />"
                        "<a href='/rango/'>Home</a>")

