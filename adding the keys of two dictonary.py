d1={'a':100,'b':200,'c':300}
d2={'a':300,'b':200,'d':400}
dic={}
for x in d1:
    for j in d2:
        if x==j:
            s=d1[x]+d2[j]
            dic[j]=s
        if x not in d2:
            dic[x]=d1[x]
        if j not in d1:
            dic[j]=d2[j]
print(dic)

