from django.shortcuts import render


# Create your views here.


def hello(request):
    return render(request, 'myapp/hello.html', {
        'n': 100,
        'fg': "ghj"
    })
