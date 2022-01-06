Num=int(input("Enter the number"))
dic={}
i=1
while(i<=Num):
    d={}
    a=input("Enter the name")
    b=int(input("Enter the number"))
    d.update({"Name":a})
    d.update({"Age":b})
    dic.update({i:d})
    i+=1
print(dic)
