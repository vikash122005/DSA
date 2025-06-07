def shuffle(nums, n):
    half = nums[n:len(nums)]
    org = []
    for i in range(n):
        org.append(nums[i])
        org.append(half[i])
    return org

nums = [2,5,1,3,4,7]
n = 3

print(shuffle(nums, n))