from django.shortcuts import render
from . import Vitrek4700driver
import time
# Create your views here.


def show_test_voltage(request):
    params = [
        ['123,2', '321', '50,1', '600', '1,41'],  # DC, AC, frequence, peak-peak, CF
        ['123,12', '321', '50,2', '600', '1,41'],
        ['123,12', '321', '50,3', '600', '1,41'],
    ]
    context = {'measurements': params}
    return render(request, 'main/index.html', context)


def show_voltage(request):
    vitrek = Vitrek4700driver.vitrek4700('172.16.4.90')
    params = []
    for i in range(10):  # this is stupid idea but now i don't know async/await. Wait 10 sec load page, bro
        time.sleep(1)
        params.append(vitrek.getmeasures())


    context = {'measurements': params}
    return render(request, 'main/index.html', context)


def show_setting(request):
    pass


def set_settings(request):
    pass


