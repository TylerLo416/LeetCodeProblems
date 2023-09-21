class Solution:
    def isPalindrome(self, s: str) -> bool:
        #2 pointers from each side, until one overlaps
        s = s.translate(str.maketrans('', '', string.punctuation))
        s = s.replace(" ","")
        s = s.lower()
        print(s)
        if len(s) <= 1:
            print('??')
            return True
        startIndex = 0
        start = s[startIndex]
        end = s[len(s)-1]
        while(startIndex < len(s)-startIndex):
            start = s[startIndex]
            end = s[len(s)-1-startIndex]
            if start != end:
                return False
            startIndex += 1
        return True 