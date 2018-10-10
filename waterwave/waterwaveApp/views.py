from django.http import HttpResponse
from django.shortcuts import render

from .models import Waterwave


def index(request):
    waterwave_list = Waterwave.objects.all()
    context = {'waterwave_list': waterwave_list}
    return render(request,'waterwaveApp/index.html',context)
