class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = 0
        jump = 0
        current_end = 0

        for i in range(len(nums)-1):
            if i + nums[i] > goal:
                goal = i + nums[i]

            if i == current_end:
                jump += 1
                current_end = goal
        return jump

        #time comp: O(n)
        #space comp: O(1)