"________METHOD - 1 O(n)________"
arr = [8,5,7,8,3,9,5]
occ = 0

while(occ < len(arr)):
    if(occ == 0):
        arr.pop(0)
        occ +=1
    else:
        occ += 1

print(arr)

"________METHOD - 2 O(1)________"

arr = [8,5,7,8,3,9,5]

print(arr[1:])


