a ='Poltavskiy shlyach street 190/1, Харків, 61034, Україна'
a1=a.rfind(',')
a2=a.find(',')
b=a[a2:a1]
a1=b.rfind(',')
print(a1)
zet=b[2:a1]
print(zet)