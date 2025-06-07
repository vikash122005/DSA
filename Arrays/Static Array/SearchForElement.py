inp = int(input("Enter a number to search: "))
arr = [1, 2, 3, 5, 9]

for i in range(len(arr)):
    if(inp == arr[i]):
        print(f"The element was found in {i}")