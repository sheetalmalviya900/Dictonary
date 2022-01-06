x={'key1': 1, 'key2': 3, 'key3':2}
y={'key1': 1, 'key2': 2, 'key3':2}
for i in x:
    for j in y:
        if i==j:
            if x[i]==y[j]:
                print(i,":",x[i])