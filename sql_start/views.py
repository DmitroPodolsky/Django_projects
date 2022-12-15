from django.shortcuts import render,get_object_or_404
from .models import First
from django.db.models import Max,Min,Avg,Count,F,Sum
# Create your views here.
def func(request):
    #date = First.objects.all()- получа'м в любом виде результат
    #date =First.objects.order_by('name')#алфавитный порядок
    date = First.objects.order_by('-id')#обратный айдишный порядок
    #for i in date:
        #i.save() - помогло моментально внести данние в бд
    return render(request,'sql_start/index.html')
def func1(request,han):
    fan=get_object_or_404(First,slug=han) # ты поймёшь
    return render(request, 'sql_start/new_1.html', {
        'join': fan
    })
def func2(request):
    date = First.objects.order_by('-rating','-budget')[:3]  # срез, сначало сортируется рейтинг и если одинаковый то будет вступать в силу бюджет
    agg = First.objects.aggregate(Max('budget'),Min('budget'),Avg('budget'),Sum('budget'))

    return render(request, 'sql_start/gg_wp.html', {
        'join': date,
        'kan': agg
    })