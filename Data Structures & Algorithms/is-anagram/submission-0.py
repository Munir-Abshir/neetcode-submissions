from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(t) != len(s)):
            return False
        else:
            return Counter(s) == Counter(t)

        