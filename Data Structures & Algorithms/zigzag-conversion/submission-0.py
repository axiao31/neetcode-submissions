class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #Input: "PAYPALISHIRING"  numRows=3
        #Output: "PAHNAPLSIIGYIR"
        if numRows == 1:
            return s

        res = [] #[P,A,H,N,A,P,L,S,I,I,G,Y,I,R]
        increment = 2 * (numRows - 1) #increment = 2*(3-1) = 4

        for i in range(numRows):
            for j in range(i, len(s), increment): 
            #start i, keep adding increment each time, stop be s 
                res.append(s[j])

                #middle rows also have a diagonal character
                if i > 0 and i < numRows - 1 and j + increment - 2 * i < len(s):
                    res.append(s[j + increment - 2 * i])
        return ''.join(res)

        #time comp: O(n)
        #space comp:O(n) for the ouput string.