class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = []

        for i in range(len(arr) - 1):
            max_val = -1
            for j in range(i + 1, len(arr)):
                if arr[j] > max_val:
                    max_val = arr[j]
            n.append(max_val)
        
        print(n)
        n.append(-1)
        return n

        #arr = [2,4,5,3,1,2]
        #       i j            4>-1        max_val= 4,    5
        # [  ]