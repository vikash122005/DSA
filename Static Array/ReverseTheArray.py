"________METHOD - 1 O(n)________"

arr = [1, 2, 3, 4]
print(arr[::-1])

"________METHOD - 2 O(n)________"

arr = [1, 2, 3, 4]
first = 0
last = len(arr) -1
while(first < last):
    arr[first],arr[last] = arr[last],arr[first]
    first += 1
    last -= 1
print(arr)