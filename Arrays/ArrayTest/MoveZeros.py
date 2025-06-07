"""_______________Method1________________"""
lst = [4, 0, 5, 0, 0, 1]
non_z = 0
leng = len(lst)
lst2 = []
for i in range(len(lst)):
    if(lst[i] != 0):
        lst2.append(lst[i])
        non_z +=1
for j in range(non_z,leng):
    lst2.append(0)
print(lst2)

"""_______________Method2________________"""

lst = [4, 0, 5, 0, 0, 1]
non_z = 0

for i in range(len(lst)):
    if(lst[i] != 0):
        lst[non_z] = lst[i]
        non_z +=1

for j in range(non_z,len(lst)):
    lst[j] = 0

print(lst)

