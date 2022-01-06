list=[{"v":"s001"},{"v":"s002"},{"vi":"s001"},{"vi":"s005"},{"vii":"s005"},
{"v":"s009"},{"viii":"s007"}]
i=0
l=[]
while(i<len(list)):
    for x in list[i]:
        l.append(list[i][x])
    i+=1
dic=[]
i=0
while(i<len(l)):
    if l[i] not in dic:
        dic.append(l[i])
    i+=1
print(dic)
        
