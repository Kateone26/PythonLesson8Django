from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # print(request)
    # return HttpResponse("<h1>hi there</h1>")
    context = {"word": "Hello World!!!!"}
    return render(request, 'home.html', context)
def about(request):
    # return HttpResponse("<h1>about</h1>")
    return render(request, 'about.html')