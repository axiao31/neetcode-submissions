class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res =0
        numsSet = set(nums)

        streak = 0
        for n in numsSet:
            if n-1 not in numsSet:
                streak += 1
                while (n+streak) in numsSet:
                    streak +=1
                res = max(res, streak)
                streak = 0
        return res
        # res = 1
        # if len(nums)==0:
        #     return 0
        # nums.sort()
        # counter = 1
        # for i in range(len(nums)-1):
        #     if nums[i+1] == 1 + nums[i]:
        #         counter +=1
        #         res = max(res, counter)
        #     elif nums[i+1] == nums[i]:
        #         continue
        #     else: 
        #         counter = 1
        # return res
        # # Time: O(Nlog(N)) Space: O(1)
        