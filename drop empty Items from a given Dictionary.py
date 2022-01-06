dic={'c1': 'Red', 'c2': 'Green', 'c3': None}
a={}
for x in dic:
    if dic[x] is  None :
        pass
    else:
        a[x]=dic[x]
print(a)