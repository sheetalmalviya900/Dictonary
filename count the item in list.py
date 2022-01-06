dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
count=0
for x in dict:
    if type(dict[x]) is list:
        count+=len(dict[x])
print("total list item is :",count)
