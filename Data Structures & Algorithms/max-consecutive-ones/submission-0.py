class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0 
        l = [] 
        n = len(nums)-1
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            
            if nums[i] == 0 or i == n:
                l.append(count)
                count = 0

        return max(l)