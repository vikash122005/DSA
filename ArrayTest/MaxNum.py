lst = [0, 0, 0, 0]
val = lst[0]
for i in range(len(lst) - 1):
    if(val < lst [i + 1]):
        val = lst[i + 1]
print(val)