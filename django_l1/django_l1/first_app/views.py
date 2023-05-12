from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    my_dictionary = {
        'insert_me': "Hello from first_app/views.py"
    }
    return render(request, 'django_l1/index.html', context=my_dictionary)
