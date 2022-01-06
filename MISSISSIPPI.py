name=input("enter the name :")
i=0
dic={}
while(i<len(name)):
    j=0
    count=0
    while(j<len(name)):
        if(name[i] == name[j]):
            count+=1
        j+=1    
    dic[name[i]]=count
    i+=1
print(dic)


# str=input("enter the name:")
# dic={}
# for x in str:
#     dic[x]=dic.get(x,0)+1
# print(dic)
