arr = [1, 2, 3, 4, 5]
val = int(input("enter the value to insert: "))
index = int(input("Enter the index position: "))
for i in range(len(arr) - 1 ,index,-1):
        arr[i] = arr[i - 1]
arr[index] = val
print(arr)