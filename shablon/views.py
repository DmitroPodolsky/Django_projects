from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from django.template.loader import render_to_string
# Create your views here.
dict1 = {'gans': 'отмечает конец весны в Северном полушарии и конец осени в Южном полушарии',
         'deva': 'отмечает конец лета в Северном полушарии и конец зимы в Южном полушарии',
         'sniper': 'отмечает конец осени в Северном полушарии и конец весны в Южном полушарии',
         'fish': 'отмечает конец зимы в Северном полушарии и конец лета в Южном полушарии',
         'gay': 'знак <i>зодиака</i> гей',
         'gay1': 'знак зодиака золото',
         'natural': 'крассава',
         }
class Dog:
    @classmethod
    def __init__(cls,a,b):
        cls.a=a
        cls.b=b
    @classmethod
    def __str__(cls):
        return f'всё по красоте {cls.a} {cls.b}'#это надо для удобного преобразования в html
def ranc(request,hey1):
    #более лучше метод,настраиваем динамическую ссылку
    dannue=dict1.get(hey1)
    enter_me={'gason':dannue,
              'gay':hey1,
              'Jack':{'lol':34,'kal':'hello'},
              'lo':[1,2,3],
              'good':Dog(5,'hi')}#принимает данные
    return render(request,'shablon/ganfan.html',context=enter_me)
    #context-отвечает за передачу данных в динамическую ссылку

def menu(request):
    enter_me={'hon':list(dict1),
              'gun':dict1}
    return render(request,'shablon/menu.html',context=enter_me)


    #revn=render_to_string('shablon/ganfan.html')
    #return HttpResponse(revn)