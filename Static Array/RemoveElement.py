
"________METHOD - 1 O(n)________"
 
arr = [9, 8, 7, 6, 5]
index = int(input("Enter a index to remove: "))

arr.pop(index)
print(arr)


"________METHOD - 2 O(n)________"

arr = [9, 8, 7, 6, 5]
index = int(input("Enter a index to remove: "))

for i in range(index,len(arr) - 1):
    arr[i] = arr[i+1]
arr[-1] = 0 
print(arr)

