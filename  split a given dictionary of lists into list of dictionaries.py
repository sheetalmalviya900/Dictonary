a={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
l=[]
d={}
li=[]
for x in a:
    for i in range(len(a[x])):
        li.append({x:a[x][i]})
print(li)

# # [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, 
# # {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]


# l=[]
# i=0
# for x in a:
#     l.append({a[0]:a[x][i],a[1]:a[x][i]})
#     print()
# i+=1
# print(l)