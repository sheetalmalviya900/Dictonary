s={8:45,4:60,7:20,9:30,2:50}
a=[]
for i in s:
    a.append(i)
i=0
while i<len(a):
    j=0
    while j<len(a):
        if a[i]<a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
        j+=1
    i+=1
n={}
j=0
while j<len(a):
    for i in s:
        if a[j]==i:
            n[i]=i
    j+=1
print(n)

