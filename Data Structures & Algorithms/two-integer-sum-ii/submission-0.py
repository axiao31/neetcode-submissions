class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while l < r:
            val = numbers[l] + numbers[r]
            if val == target:
                return [l+1, r+1]
            if val < target and l < r:
                l+=1
            elif val > target and r > l:
                r-=1
            
