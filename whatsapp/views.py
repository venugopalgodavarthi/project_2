from django.http import HttpResponse
from django.shortcuts import render


def login(request):
    class college:
        col_name = 'pys'

        def __init__(self, name, age, email):
            self.name = name
            self.age = age
            self.email = email

    return render(request=request, template_name='login.html',
                  context={'b': 100, 'a': True, 'li': ['a', 'b', 'c', 'hello'], 'di': {'x': 100, 'y': 500}, 'sai': college('sai', '26', 'sai@gmail.com')})


def upper_case(request, name):
    wish = f'''Hello,\n
     my dear {name.upper()},

     happy birthday to you.

     Thank you Dear. 
    '''
    return HttpResponse(wish)


def about(request, x, y):
    return render(request=request, template_name='about.html', context={'a': 'hello', 'b': y, 'l': [10, 200, 100, 50, 60], 'd': None})


def base(request, data):
    return render(request=request, template_name='base.html', context={'data': data.lower()})


def sample(request):
    d = [{'name': 'raja', 'email': 'raja@gmail.com', 'age': 26, 'phone': 9966885544},
         {'name': 'rani', 'email': 'rani@gmail.com',
             'age': 25, 'phone': 9966889998},
         {'name': 'dinga', 'email': 'dinga@gmail.com',
             'age': 24, 'phone': 8866885544},
         {'name': 'dingi', 'email': 'dingi@gmail.com',
             'age': 23, 'phone': 9976885544},
         {'name': 'ramu', 'email': 'ramu@gmail.com', 'age': 28, 'phone': 998885544}]
    return render(request=request, template_name='sample.html', context={'data': d})
