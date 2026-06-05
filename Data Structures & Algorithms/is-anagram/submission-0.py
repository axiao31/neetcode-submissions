class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #get every unqiue letter
        #compare, if all the letter same as each other reutrn true, otherwise return false

        # s_set = set(s)
        # t_set = set(t)

        # if len(s) == len(t) and s_set == t_set:
        #     return True
        # return False

        # s_count = Counter(s) #s="racecar", 'r': 2, 'a': 2, 'c': 2, 'e': 1
        # t_count = Counter(t) # t="carrace", 'r': 2, 'a': 2, 'c': 2, 'e': 1
        
        # if len(s) == len(t) and s_count == t_count:
        #     return True
        # return False

        if len(s) != len(t):
            return False

        count = [0]*26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        for i in range(len(count)):
            if count[i] != 0:
                return False
        return True