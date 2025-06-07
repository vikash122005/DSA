lst = [100]
val = False
if(len(lst) == 1):
    val = True
    print(val)
else:
    for i in range(len(lst) - 1):
        if(lst[i] < lst[i + 1]):
            val = True
        elif(lst[i] >= lst[i+1]):
            val = False
            break

print(val)

