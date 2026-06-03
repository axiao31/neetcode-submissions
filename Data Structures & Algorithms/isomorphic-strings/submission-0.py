class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}

        for i in range(len(s)):
            dic1[s[i]] = i

        for h in range(len(t)):
            dic2[t[h]] = h

        for j in range(len(s)):
            if dic1[s[j]] != dic2[t[j]]:
                return False
        return True