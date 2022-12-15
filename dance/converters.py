class fanConvert:
    regex = "[0-9]{4}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d'%value
#ключевые даннве при создании корвертора, ты ещё слабо это понимаешь
class floatConvert:
    regex = "[+-]?([0-9]*[.])?[0-9]+"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)