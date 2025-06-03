def remove_duplicates(nums):
    curr = 0
    for i in range(1,len(nums)):
        if(nums[curr] != nums[i]):
            curr +=1
            nums[curr] = nums[i] 
    return curr + 1

nums = [1, 1, 2]
print(remove_duplicates(nums))