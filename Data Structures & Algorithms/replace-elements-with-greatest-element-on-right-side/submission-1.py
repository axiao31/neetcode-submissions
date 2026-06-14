class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n #value is 0 and want the length of n  [0, 0, 0, 0, 0, 0]
        rightMax = -1
        for i in range(n - 1, -1, -1):
            ans[i] = rightMax
            rightMax = max(arr[i], rightMax)
        return ans

        #arr = [2, 4, 5, 3, 1, 2]  rightMax= 5
        #ans = [5, 5, 3, 2, 2,-1]                   