list=[{'item': 'item1', 'amount': 400}
        ,{'item': 'item2', 'amount': 300}, 
        {'item': 'item1', 'amount': 750}]
dic={}
for x in list:
        for j in x:
                # print(j)
                dic[x[j]]=x[j] 
print(dic)


# ({'item1': 1150, 'item2': 300})


# a={"an":1,"ab":2}
# for i in a:
#         print(a[i])