arr = [4, 2, 4, 3, 2, 4]

visited = [False] * len(arr) 

for i in range(len(arr)):
    if(visited[i]):
        continue
    count = 1
    for j in range(i+1,len(arr)):
        if(arr[i] == arr[j]):
            count +=1
            visited[j] = True
    print(f"Element: {arr[i]}, Frequency {count}")
