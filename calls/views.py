from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello(request):
    return HttpResponse("hello world")


def index(request):
    data = """
        <html>
        <head><title>index page</title></head>
        <body>
        <div>
        <h1>welcome to index page</h1>
        </div>
        </body>
        </html>"""
    return HttpResponse(data)


def home(request):
    return render(request=request, template_name="home.html")
