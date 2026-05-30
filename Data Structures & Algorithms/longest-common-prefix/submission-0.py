class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #find the most short string, then can now how long of the prefix for each string
        #use the shorter string to compare with 
        #strs = ["flower","flow","flight", "dog"]
        #prefix = dog, index 0 = d
        #strs[j][i], index 0 = flower --> indexx 0 = f
        prefix = min(strs, key=len)  #find the shorter string
        result = "" 
        for i in range(len(prefix)):
            for j in range(len(strs)):
                if prefix[i] != strs[j][i]: #compare
                    return result
            result += prefix[i]  #if yes, add the letter to the result
        return result