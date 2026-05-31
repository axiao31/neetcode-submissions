class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = sorted(ransomNote)
        m = sorted(magazine)
        i = 0
        j = 0
        while i < len(r) and j  < len(m):
            if r[i] == m[j]:
                i+=1
            j+=1
        return i == len(r)