A=[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'},
 {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
i=0
l=[]
while(i<len(A)):
    if "#FF0000" in A[i].values():
        A.remove(A[i])
    i+=1
print(A)


