class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        if len(s) != len(t):
            return False
        for i in range(len(t)):
            map[t[i]] = 1 + map.get(t[i], 0)
        for i in s:
            if map.get(i, 0) != 0:
                map[i] -= 1
            else:
                return False
        return True
