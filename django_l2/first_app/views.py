from django.shortcuts import render

# Create your views here.


def index(request):
    my_dict = {'insert_content': "Hello from django_l2/first_app/views.py/index"}
    return render(request, 'first_app/index.html', context=my_dict)
