dic={"1":['a','b'],"2":['c','d']}
x=list(dic.values())
print(x)
for i in x[0]:
    for k in x[1]:
        print(i+k)