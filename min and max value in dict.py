dic={1:8,67:3,77:46,8:23456,55:98,3:6,6:8987}
max=0
for x in dic:
    if dic[x]>max:
        max=dic[x]
print("maximum value of dictonary is :",max)

dic={10:8,1:3,77:46,55:98,3:6}
min=dic[10]
for x in dic:
    # min=dic[x]
    if dic[x]<min:
        min=dic[x]
print("maximum value of dictonary is :",min)