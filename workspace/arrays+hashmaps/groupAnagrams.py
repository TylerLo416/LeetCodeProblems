from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #array of each letter, everytime a letter in the string is found,
        #increment by 1. this gives us the anagram key.
        #map each string to an anagram key.
        soln = defaultdict(0)
        for s in strs:
            alphabet = [0]*26

            for c in s:
                alphabet[ord(c)-ord("a")] += 1
                soln[alphabet].append(s)
        return soln