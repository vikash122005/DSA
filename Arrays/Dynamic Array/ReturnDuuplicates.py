def duplicates(arr,seen,lst):
    for i in arr:
        if i in seen:
            lst.append(i)
        seen.add(i)
    return lst

arr = [8,5,9,7,8,5,3,4,1,9,2,4]
seen = set()
lst = []
print(duplicates(arr,seen,lst))