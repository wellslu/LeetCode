class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = ''
        for i in s:
            if 97 <= ord(i) <= 122 or 48 <= ord(i) <= 57:
                new_s+=i
        num = len(new_s) / 2
        if len(new_s) % 2 == 1:
            if new_s[:int(num)] == new_s[int(num)+1:][::-1]:
                return True
            else:
                return False
        else:
            if new_s[:int(num)] == new_s[int(num):][::-1]:
                return True
            else:
                return False
