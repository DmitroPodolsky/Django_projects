from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.core.validators import MinValueValidator,MaxValueValidator #валидаторы это ограничители данных, мы не можем просто к примеру ыыести минусовый рейтинг смотри внизу
from django.db.models import Max,Min,Avg,Count,F,Sum #функции агрегации(объеденение)

#здесь идёт работа с базой данных, классы- таблицы, экземпляры-данные
# Create your models here. чекай бд
class Ford(models.Model):
    floor = models.IntegerField()  # целые числа
    cabinet = models.IntegerField()  # целые числа
    def __str__(self):
        return f'этаж {self.floor}, кабинет {self.cabinet}'
class Third(models.Model):
    MAN = 'M'
    WOMEN = 'W'  # переменные должны иметь одинаковую длину символов
    Genders = [
        (MAN, 'Man'),
        (WOMEN, 'Women')
    ]
    actor_name=models.CharField(max_length=100,default='Джеки')
    actor_famale=models.CharField(max_length=100,default='Чан')
    ford=models.OneToOneField(Ford,on_delete=models.SET_NULL,null=True,blank=True)
    gender=models.CharField(max_length=1,choices=Genders,default=MAN)
    def __str__(self):
        if self.gender==self.MAN:
            return f'мужчина {self.actor_name} {self.actor_famale}'
        elif self.gender==self.WOMEN:
            return f'женщина {self.actor_name} {self.actor_famale}'
class Second(models.Model):
    sensei_name=models.CharField(max_length=100,default='Джеки')
    sensei_famale=models.CharField(max_length=100,default='Чан')
    def __str__(self):
        return f'{self.sensei_name} {self.sensei_famale}'
class First(models.Model):
    MAN='Man'
    WOM='Women'#переменные должны иметь одинаковуюдлину символов
    CURRENCY_CHOISES=[
        (MAN,'Man'),
        (WOM,'Women')
    ]
    name=models.CharField(max_length=40)#указываем что это должно быть строкой
    rating=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)])#целые числа
    year=models.IntegerField(null=True,blank=True)#тоесть мы словно говорим что значение может быть пустым, blank - мы указывавем что поле может быть пустым
    budget=models.IntegerField(default=10001)#мы указываем стартовое значение которое может быть
    slug=models.SlugField(default='',null=False)#слаг поле - работает как redirect
    currency=models.CharField(choices=CURRENCY_CHOISES,max_length=5,default=MAN)#уставливаем это, называется Choises_field
    second = models.ForeignKey(Second,on_delete=models.PROTECT,null=True,blank=True)#выполнение связи один ко многим с помощью Second
    #PROTECT - отвечает за то что мы не можем удалить те данные которые уже связаны с бд, можно использовать CASCADE
    third = models.ManyToManyField(Third)#выполнение связи многие ко многим
    #переопределяем функцию родителя
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(First,self).save(*args,**kwargs)
    def __str__(self):
        return f'{self.name} - {self.rating}%'# можно не запускать миграции(не влияет на бд)
    def get_url(self):
        return reverse('name',args=[self.slug])
class HH(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])  # целые числа
class Cities(models.Model):
    city=models.TextField()
    def __str__(self):
        return self.city
class Hotels(models.Model):
    name = models.TextField()
    adress = models.TextField()
    photo = models.TextField()
    description = models.TextField()
    city = models.ForeignKey(Cities, on_delete=models.PROTECT, null=True,blank=True) # выполнение связи один ко многим с помощью Second
    def __str__(self):
        return self.name
    #выводит ответ на наш поисковый запрос
#после любого изменения в миграции должен поочерёдно вводить две команды:
#python manage.py makemigrations
#python manage.py migrate

#Python manage.py shell - отвечает за команду вноса данных и потом в консоле его добавлять
#from sql_start.models import First # выбрали что будем вносить
#a = First(name='Sbastian',rating=100) - вносим данные, смотри там
#First.objects.create(name='hi',rating=0) - как вариант
#First(name='fan',rating=50).save() - в одну строку
#>>> a.save() - сохраняем в бд
#Python manage.py shell_plus --print-sql - более удобно

#про запросы к бд
#First.objects.all()[2:] - срез запроса как в списке
#a = First.objects.all()[2] - переменная а присвоила значения ключей
#a.name - получит значение

#про изменения\удаления в бд
#a.name='7'
#a.save()

#фильтрация данных
# First.objects.get(id=5) - будет искать такой, не работает с несуществуищими(еррор) и мы не можем искать по тем значениям которые дублируются в других таб
#First.objects.filter(budget=10001) - работает как гит но возращает кол-во таблиц и нету еррора в случае если ничего не находит
#First.objects.filter(budget__gte=10001)
'''операции равенства:
__gt больше
__lt меньше
__gte + равно
__lte + равно
First.objects.exclude(budget=10001) - неравно
'''
# First.objects.filter(budget__gte=10001,year__isnull=False) - двойное условие
# First.objects.exclude(year__isnull=False).filter(budget__gte=10001)
#__contains__ - содержит
#союзы and or
#from django.db.models import Q - импортируем функцию обязательно
#First.objects.filter(Q(rating=80))- можем это делать без союзов
#First.objects.filter(Q(rating__gt=60) & Q(id__in=[5,7,9])) - & - and
#First.objects.filter(Q(rating__gt=60) | Q(name='Franco')) - | - or
#First.objects.filter(Q(rating__gt=60) & ~Q(id__in=[4,6,9,5])) - ~Q - not ...
#First.objects.filter(Q(rating__gt=60) | ~Q(id__in=[4,6,9,5]), Q(year__isnull=True)) - (if or if) and if

#функции агрегации(объеденение)

#First.objects.aggregate(Max('budget'))
#First.objects.aggregate(Max('budget'),Min('budget'),Avg('budget'),Sum('year'))

