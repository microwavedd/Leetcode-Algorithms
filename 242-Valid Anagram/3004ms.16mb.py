#This one is pretty slow
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t = t.lower()
        if len(s) != len(t):
            return False
        for i in s.lower():
            if s.count(i) != t.count(i):
                return False
        return True