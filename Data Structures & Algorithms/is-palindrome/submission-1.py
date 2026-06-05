class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = ''.join(e for e in s if e.isalnum()).lower()
        for i in range(0,int(len(news)/2)):
            if news[i] != news[len(news)-i-1]:
                return False
        return True