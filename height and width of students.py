a={'Cierra Vega': (6.2, 71), 'Alden Cantrell': (5.9, 65), 
'Kierra Gentry': (6.0, 68), 'Pierre Cox': (6.8, 76)}
dic={}
for x in a:
    if a[x][0]>=6 and a[x][1]>=70:
        dic[x]=a[x]
print(dic)