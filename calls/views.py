from django.shortcuts import render
from django.http import HttpResponse
from calls.forms import personal_form
from calls.models import personal

# Create your views here.


def register(request):
    form = personal_form()  # generate the html content
    print(form)
    if request.method == 'POST':
        form = personal_form(request.POST)  # validation
        if form.is_valid:  # verify the data is valid or not
            # form.save()
            return HttpResponse("data is stored")
        else:
            return HttpResponse("data is not stored")
    return render(request=request, template_name="register.html", context={'form': form})


def update(request, pk):
    data = personal.objects.get(id=pk)
    print(data)
    form = personal_form(instance=data)  # generate the html content
    if request.method == 'POST':
        form = personal_form(request.POST, instance=data)  # validation
        if form.is_valid:  # verify the data is valid or not
            form.save()
            return HttpResponse("data is stored")
        else:
            return HttpResponse("data is not stored")
    return render(request=request, template_name="register.html", context={'form': form})


def list_details(request):
    res = personal.objects.all()
    return render(request=request, template_name='details.html', context={'data': res})


def delete(request, pk):
    try:
        res = personal.objects.get(id=pk)
        if request.method == "POST":
            res = personal.objects.get(id=pk).delete()
            return HttpResponse('data is deleted')
    except:
        res = None
    return render(request=request, template_name='delete.html', context={'id': res})


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
