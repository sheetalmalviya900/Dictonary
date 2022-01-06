dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
max=0
max2=0
max3=0
key=0
key2=0
key3=0
k=[]
for x in dict:
    if dict[x]>max:
        max3=max2
        key3=key2
        max2=max
        key2=key
        max=dict[x]
        key=x
    elif dict[x]>max2:
        max3=max2
        key3=key2
        max2=dict[x]
        key2=x
print([key,key2,key3])
