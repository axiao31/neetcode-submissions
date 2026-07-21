class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #each element in array = maximum jump length
        #return True if reach the last index, otherwise return False
        goal = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0

        #time comp: O(n)
        #space comp: O(1)