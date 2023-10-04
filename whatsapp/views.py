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
