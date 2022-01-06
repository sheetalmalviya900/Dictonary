list1=[
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
     
     ]
l=[]
for x in list1:
    for i in x:
        if x[i] not in l:
            l.append(x[i])
print(l)
