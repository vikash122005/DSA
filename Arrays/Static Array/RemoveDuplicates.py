class Solution(object):
    def removeDuplicates(self, nums):
        fst = 0
        for i in range(1,len(nums)):
            if(nums[fst] != nums[i]):
                fst += 1
                nums[fst] = nums[i]
                
        
        return fst + 1
