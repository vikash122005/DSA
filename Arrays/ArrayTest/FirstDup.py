lst = [10, 20, 30, 40]
dist = set()
dup = -1  

for i in lst:
    if i in dist:
        dup = i
        break  
    dist.add(i)

print(dup)





