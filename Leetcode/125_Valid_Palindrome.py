class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = str()
        for i in s.lower():
            if i.isalpha():
                alpha += i
            elif i.isdigit():
                alpha += i
                
        return alpha == alpha[::-1]






# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         alpha = str()
#         for i in s.lower():
#             if i.isalpha() or i.isdigit():
#                 alpha += i
#         if alpha == alpha[::-1]:
#             return True
#         else:
#             return False
        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = str()
        for i in s.lower():
            if i.isalpha() or i.isdigit():
                alpha += i
        if alpha == alpha[::-1]:
            return True
        return False