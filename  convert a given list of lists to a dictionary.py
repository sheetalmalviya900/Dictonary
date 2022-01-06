li=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'],
 [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
dic={}
for i in range(len(li)):
    c=[]
    for j in range(1,len(li[i])):
        c.append(li[i][j])
        dic.update({li[i][0]:c})
print(dic)