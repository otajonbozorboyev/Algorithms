# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         return len(s.split()[-1])



# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         result = 0
#         length = len(s)
#         for i in range(length-1, -1, -1):
#             if s[i].isalpha():
#                 result += 1
#             elif s[i] == ' ' and result != 0:
#                 break
#         return result
obj1 = Solution()
s = "Hello World    " # ['Hello', 'World']
s1 = "a "
print(obj1.lengthOfLastWord(s))



# Bu ham ishladi faqat barcha kombenatsiyalar uchun emas.

        # length = 0
        # for i in range(len(s)-1, 0, -1):
        #     if s[i] == ' ':
        #         if length == 0:
        #             continue
        #         return length
        #     length += 1
        # return length