from django.shortcuts import render, redirect

from myapp import models
from myapp.models import Cat


# Create your views here.


def hello(request):
    if request.POST:

        cat = models.Cat()
        age = request.POST.get('age')
        print(age)
        cat.age = age

        color = request.POST.get('color')
        print(color)
        cat.color = color

        gender = request.POST.get('gender')
        print(gender)
        if gender=="man":
            cat.gender=0
        elif gender=="woman":
            cat.gender=1
        else:
            raise Exception('Invalid gender')

        cat.save()

        return redirect('/lee')




    return render(request, 'myapp/hello.html', {
        'n': 100,
        'fg': "ghj"
    })
def lee(request):
    cats = Cat.objects.all()
    return render(request, 'myapp/lee.html',{
        'cats': cats
    })
