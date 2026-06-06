class Solution:
    def isPalindrome(self, s: str) -> bool:
        # cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', s)
        # s_reve = cleaned_text[::-1]
        # if cleaned_text.lower() == s_reve.lower():
        #     return True
        # return False

        l, r = 0, len(s)-1

        while l < r:
            while l < r and not s[l].isalnum():
                l+=1
            while r > l and not s[r].isalnum():
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l,r = l+1, r-1
        return True
            