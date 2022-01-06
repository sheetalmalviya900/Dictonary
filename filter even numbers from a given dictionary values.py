dic={'V': [1, 4, 6,5,10], 'VI': [1,4,7, 12], 'VII': [1,5,6]}
# for x in dic:
#     for j in dic[x]:
#         if j%2==0:
#             pass
#         else:
#             dic[x].remove(j)
#         # print(dic[x])
# print(dic)


for x in dic.values():
    for j in x:
        if j%2==0:
            pass
        else:
            x.remove(j)
print(dic)