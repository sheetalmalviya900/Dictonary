she={1:20,2:10,3:40,4:30,5:50}
# she={1:20,2:20}
product=1
for x in she:
    product*=x
    product*=she[x]
print("product of item is",product)
