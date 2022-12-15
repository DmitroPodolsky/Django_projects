from django.contrib import admin,messages
from .models import First,Second,Third,Ford,Hotels,Cities
from django.db.models import QuerySet,Q
# Register your models here.
admin.site.register(Second)
admin.site.register(Third)
admin.site.register(Ford)
admin.site.register(Hotels)
admin.site.register(Cities)
class Filter_rate(admin.filters.SimpleListFilter):
    title = 'filter rate'#название фильтра
    parameter_name = 'Rangon'#имя url
    def lookups(self, request, model_admin):
        return [
            ('<40','low'),
            ('from 40 to 69', 'normal'),
            ('from 69 to 89', 'good'),
            ('>=90', 'incriedble')
        ]# '<40'-отвечает за кусочек url,'low' - вывод кнопки фильтра
    def queryset(self, request, queryset : QuerySet):
        if self.value()=='<40':
            return queryset.filter(rating__lt=40)
        if self.value()=='from 40 to 69':
            return queryset.filter(Q(rating__lt=70) & Q(rating__gte=40))
        if self.value()=='from 69 to 89':
            return queryset.filter(Q(rating__lt=90) & Q(rating__gte=70))
        elif self.value()=='>=90':
            return queryset.filter(rating__gte=90)
        else:
            return queryset.filter()

@admin.register(First)
class AdminFirst(admin.ModelAdmin):
    #fields = ['name','rating']#можем только эти данные вносить когда создаём таблицу
    #exclude = ['slug']#по-лучше fields, исключает данные которые будем вносить в таб
    readonly_fields = ['budget']#пользователю будет видно, но не сможет вносить данные
    prepopulated_fields = {'slug':('name',)}# сложно объяснить тебе, это чтобы поля пр вводе сразу заполнялись
    list_display = ['name','rating','budget','currency','figma','second']#это для более разширенных настроек, отображение данных
    list_editable = ['rating','budget','currency','second']#для изменений данных, нельзя вносить первую таб так как это ссылка по сути
    filter_horizontal = ['third']#отвечает за более удобное отображение таблицы когда работает множества к множеству горизонтально
    #filter_vertical = ['third']#отвечает за более удобное отображение таблицы когда работает множества к множеству вертикально
    ordering = ['-budget']#аналогично как в моудлях,фильтры
    list_per_page = 5#отвечает за странички в бд
    actions = ['set_Wumen','set_Men']#регитрируем действие
    #заносим названия методов
    search_fields = ['name__startswith','rating']#создём поисковую панель
    list_filter = ['name',Filter_rate]#создаём фильтровую панель
    # заносим названия методов
    @admin.display(ordering='-rating')#сортируем
    def figma(self,lol: First):
        #аннатировали чтобы были видны подсказки
        if lol.rating<50:
            return 'bref'
        if lol.rating<80:
            return 'normal'
        return 'oh my god'
    #создание действия админки
    @admin.action(description='пол Мужчина')
    def set_Men(self,request,queryset:QuerySet):
        count = queryset.update(currency=First.MAN)
        self.message_user(request, f'обновлено {count} записей',messages.ERROR)#уведомление c еррор
    @admin.action(description='пол Женщина')
    def set_Wumen(self, request, queryset: QuerySet):
        count = queryset.update(currency=First.WOM)
        self.message_user(request,f'обновлено {count} записей')

#admin.site.register(First) #регистрируем из модели класс который отвечает за бд и с этого места мы с админки делаем что хотим