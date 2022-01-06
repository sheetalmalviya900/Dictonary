s={'bijender':45,'deepak':60,'ishu':67,'param':20,'anjili':30,'roshini':50}
a=[]
for i in s:
    a.append(s[i])
i=0
while i<len(a):
    j=0
    while j<len(a):
        if a[i]<a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
        j+=1
    i+=1
n={}
j=0
while j<len(a):
    for i in s:
        if a[j]==s[i]:
            n[i]=s[i]
    j+=1
print(n)

# a=[]
# for i in s:
#     a.append(s[i])
# i=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         if a[i]>a[j]:
#             temp=a[i]
#             a[i]=a[j]
#             a[j]=temp
#         j+=1
#     i+=1
# n={}
# j=0
# while j<len(a):
#     for i in s:
#         if a[j]==s[i]:
#             n[i]=s[i]
#     j+=1
# print(n)