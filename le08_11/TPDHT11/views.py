from datetime import datetime, timedelta

import telepot
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView

from .models import Dht
import csv


def sendtele():
    token = '2112940431:AAFvEGA8V0ZXvn0Jao1GsFW5UqMIdZe-qlk'
    rece_id = 2115040562
    bot = telepot.Bot(token)
    bot.sendMessage(rece_id, 'la température depasse la normale')
    print(bot.sendMessage(rece_id, 'OK.'))


def data(request):
    tab1 = Dht.objects.all()
    s = {'tab1': tab1}
    return render(request, 'app/tables.html', s)

def Dater(request):
    tab = Dht.objects.all()
    if request.method == 'POST':
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        D = Dht.objects.filter(date__range=[start_date, end_date])
        print(D)

    s = {'tab': tab, 'D': D}
    return render(request, 'app/chart.html', s)


def home(request):
    return HttpResponse('bonjour à tous')


def exp_csv(request):
    obj = Dht.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=DHT.csv'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Temp', 'HUM', 'DT'])
    studs = obj.values_list('id','temp', 'hum', 'dt')
    for std in studs:
        writer.writerow(std)
    return response

def dht11(request):
    tab = Dht.objects.order_by('id')
    tab1 = Dht.objects.values()
    list2 = (list(tab1))[-1]
    temp1 = list2['temp']
    hum1 = list2['hum']
    dt1 = list2['dt']
    list1=(list(tab1))[-3:]

    s = {'tab': tab,"list1":list1,"list2":list2,"temp1":temp1,"hum1":hum1,"dt1":dt1}

    return render(request, 'app/app.html', s)

def chart(request):
    tab = Dht.objects.order_by('id')
    tab1 = Dht.objects.values()
    list2 = (list(tab1))[-1]
    temp1 = list2['temp']
    hum1 = list2['hum']
    dt1 = list2['dt']
    list1=(list(tab1))[-7:]

    if temp1 > 40 :
        send_mail(
            'température dépasse la normale,' + str(temp1),
            'anomalie dans la machine le,' + str(dt1),
            'yassine.ayat@ump.ac.ma',
            ['yassine1960ayat@gmail.com'],
            fail_silently=False,
        )

    s1 = {'tab': tab,"list1":list1,"list2":list2,"temp1":temp1,"hum1":hum1,"dt1":dt1}

    return render(request, 'app/charts.html', s1)


class EditorChartView(TemplateView):
    template_name = 'app/charts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tab"] = Dht.objects.all()
        return context


class EditorChartView1(TemplateView):
    template_name = 'app/app.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tab"] = Dht.objects.all()
        context["tab1"] = Dht.objects.last()
        context['now'] = datetime.now()
        context['t'] = (context['now']-context["tab1"].dt)
        return context
