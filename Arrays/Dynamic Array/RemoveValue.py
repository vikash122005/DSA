lst = [1, 2, 3, 2, 4, 2]
value = 2
occ = 0

while(occ < len(lst)):
    if(lst[occ] == value):
        lst.pop(occ)
    else:
        occ += 1


print(lst)