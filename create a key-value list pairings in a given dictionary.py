dic={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'],
 4: ['Lynne Foster'], 5: ['Zachary Simon']}
for x in dic:
    if type(dic[x]) is list:
        num=str(dic[x][0])
        dic[x]=num
print(dic)


# (1,2,3,4)
# 1
# 2
# 3
# 3
# 4
# 5
# 10