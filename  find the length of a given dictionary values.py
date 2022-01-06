dic={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# dic={'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
d={}
for x in dic:
    if dic[x] not in d:
        d[dic[x]]=len(dic[x])
print(d)