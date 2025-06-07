def duplicate(arr):
    for i in arr:
        if i in seen:
            return True
        seen.add(i)
    return False

arr = [1, 2, 3, 4, 2]
seen = set()
duplicate(arr),seen