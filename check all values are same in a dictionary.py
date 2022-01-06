dic={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 13, 'Pierre Cox': 12}
k=dic["Cierra Vega"]
count=0
for x in dic:
    if dic[x]==k:
        count+=1
if count==len(dic):
    print("True")
else:
    print("False")