# class Solution:
#     def diagonalSum(self, mat) -> int:
#         first_sum = 0
#         second_sum = 0
        
#         for n in range(len(mat)):
#             first_sum += mat[n][len(mat) - n - 1]
        
#         helper = 1
#         for n in range(len(mat)):
#             second_sum += mat[n][len(mat[n]) - helper]
#             helper += 1
        
#         if len(mat) % 2 == 0:
#             return first_sum + second_sum
        
#         nums = list(range(len(mat)))
#         avarage = sum(nums) // len(nums)
#         return first_sum + second_sum - mat[avarage][avarage]
    



# result = 0
#         length = len(mat)
        
#         for i in range(length):
#             if i == length - i - 1:
#                 result += mat[i][i]
#             else:
#                 result += mat[i][i] + mat[i][length - i - 1]
                
#         return result
