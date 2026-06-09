class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        steps = k % len(nums)

        while steps != 0:
            nums.insert(0, nums.pop())
            steps -= 1