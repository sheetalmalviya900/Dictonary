# dict = {
#     'a':50, 
#     'b':58, 
#     'c':56,
#     'd':40, 
#     'e':100, 
#     'f':20
#     }
dict={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}

max=0
max2=0
max3=0
max4=0
k=[]
for x in dict:
    if dict[x]>max:
        max4=max3
        max3=max2
        max2=max
        max=dict[x]
    elif(dict[x]>max2):
        max4=max3
        max3=max2
        max2=dict[x]
print(max,max2,max3,max4)