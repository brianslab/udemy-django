from django.shortcuts import render
from django.http import HttpResponse

from first_app.models import Webpage, Topic, AccessRecord

# Create your views here.


def index(request):
    webpages = AccessRecord.objects.order_by('date')
    dates = {'access_records': webpages}

    return render(request, 'first_app/index.html', context=dates)
