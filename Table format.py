my= {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# list=[]
# k=0
# for i,j in my.items():
#     print(i,end=" ")
#     list.append(j)
# print("\n")
# for i in range (0,len(list)):
#     for j in range (0,len(list[i])):
#         print(list[j][i],end=" ")
#     print()



print("c1","c2","c3")
c1,c2,c3=my.values()
for i in range(len(c1)):
    for j in range(len(c2)):
        for k in range(len(c3)):
            if i==j and j==k:
                print(c1[i],c2[j],c3[k])
