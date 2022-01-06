dic1={1:10, 2:20}
dic2={3:30,7:40}
dic3={5:50,6:60}


# for x in dic2:
#     dic1[x]=dic2[x]
# for x in dic3:
#     dic1[x]=dic3[x]
# print(dic1)

# D={**dic1,**dic2,**dic3}
# print(D)


dic1.update(dic2)
dic1.update(dic3)
print(dic1)