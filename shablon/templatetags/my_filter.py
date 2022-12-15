from django import template
register = template.Library()
@register.filter(name='fan')#регистрация фильтра с названием его
def fan(value):
    return value+' fan'
#можем любую функцию делать
#по-поводу документации:
#https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa1VubjJCT1RmWlRPVUFaRzZSOEdacG9xX0dLZ3xBQ3Jtc0tsVmFsYUxreFM5S2ZROEJhRHlLNEhYeElESUdkdE85YWpJb2Q0NS1MNXI2SW85WDRYWEswUlF0Q0ZVSjl6YnotcEY2NWNqZFdmOGstNVlEMjlOblNBTkxVZ3E0NjZSMll4aElUMS03NlVFSUluUEtFNA&q=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2F3.2%2Fhowto%2Fcustom-template-tags%2F&v=47h3HAL1YtQ