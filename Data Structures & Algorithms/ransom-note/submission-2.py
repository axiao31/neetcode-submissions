class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = Counter(ransomNote)
        m = Counter(magazine)

        if r & m == r:  #symbol '&': It returns a new set containing only the elements that exist in both sets
            return True
        return False

        #ransomNote aa, r a:2 
        #magazine ab, m a:1 b:1
        #r & m  a:1