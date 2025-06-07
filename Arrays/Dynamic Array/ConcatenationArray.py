def getConcatenation(nums):
    length = len(nums)
    capacity = len(nums) * 2
    ans = [0] * capacity
    for i in range(len(nums)):
        ans[i] = nums[i]
    hol = 0
    for j in range(length,capacity):
        ans[j] = nums[hol]
        hol = hol + 1
    return ans

nums = [1,2,3]
print(getConcatenation(nums))