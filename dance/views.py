from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, \
    HttpResponseRedirect  # это отвечает за ответ пользователю который сделал запрос через url к серверу
from django.urls import reverse
from django.template.loader import render_to_string
# redDirect- отвечает за переопределение ссылки ответа

# Create your views here. тут можно создавать функции и классы только
dict1 = {'gans': 'отмечает конец весны в Северном полушарии и конец осени в Южном полушарии',
         'deva': 'отмечает конец лета в Северном полушарии и конец зимы в Южном полушарии',
         'sniper': 'отмечает конец осени в Северном полушарии и конец весны в Южном полушарии',
         'fish': 'отмечает конец зимы в Северном полушарии и конец лета в Южном полушарии',
         'gay': 'знак зодиака гей',
         'gay1': 'знак зодиака золото',
         'natural': 'крассава',
         }


def ok(request,sign):
    return HttpResponse(f'<h1>tyhan password - {sign}</h1>')
def ok1(request,sign):
    return HttpResponse(f'<h1>tyhan password - {sign}</h1>')
# def gay1(request):
# return HttpResponse('знак зодиака золото')
def menu(request):
    jan = list(dict1)
    re = ''
    for sign in jan:
        main_lol = reverse("hello_druid", args=[sign])
        re += f'<h1><li><a href="{main_lol}">{sign.title()}</a></li></h1>'
    jan = f'''
    <ol>
    {re}
     </ol>
     '''
    return HttpResponse(jan)
'''1.li-отвечает за столбики, он их создаёт
2.a- отвечает за тег слова(тоесть может иметь ссылку
3.href- отвечает за ссылку на это слово тег
4.ol- отвечает за подсчёт li(номерует)'''

def key(request, hello: str):
    #a = dict1.get(hello, None)
    vann=render_to_string('dance/basar.html')#все операции строк берёт на себя html
    return HttpResponse(vann)
    #if a != None:
        #return HttpResponse(f'<h2>{a}</h2>')  # h2-заголовок(немного html)
    #else:
        #return HttpResponseNotFound(f'ты попутал берега, такого нету - {hello}')
        # return HttpResponse('лох') #в случае если не находит другие ссылки
        # if hello == 'gay':
        # return HttpResponse('знак зодиака гей')
        # elif hello == 'gay1':
        # return HttpResponse('знак зодиака золото')
        # elif hello == 'natural':
        # return HttpResponse('крассава')это больше не пригодится из-за конвертирования


def key_number(request, hello: int):
    a = list(dict1)
    if hello <= len(a):
        if hello == 0:
            return HttpResponseNotFound(f'this is number {hello}')  # переодресация ссылки на ключ словаря для удобства
        b = a[hello - 1]
        main_lol = reverse("hello_druid", args=(b,))
        return HttpResponseRedirect(main_lol)
    else:
        return HttpResponseNotFound(f'this is number {hello}')
