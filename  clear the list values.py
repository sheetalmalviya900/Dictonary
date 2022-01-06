a={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': 12}

for x in a:
    if type(a[x]) is list:
        a[x]=[]
print(a)