# [2,2,1] (to set) -> (2,1)
# (2,1) (to list) -> [2,1]
# [2,1] * 2 -> [2,1,2,1]
# (sum) [2,1,2,1] -> 6
# (sum) [2,2,1] -> 5
# (return) 6 - 5 => 1

class Solution:
    # def singleNumber(nums):
#     to_set = set(nums)          # (2,1)
#     to_list = list(to_set)      # [2,1]
#     to_list = to_list * 2       # [2,1,2,1]
#     first_sum = sum(to_list)    # 6
#     second_sum = sum(nums)      # 5
#     return first_sum - second_sum

    # def singleNumber(nums):
#     new_list = list(set(nums)) * 2
#     return sum(new_list) - sum(nums)

    def singleNumber(nums):
        return sum(list(set(nums))*2) - sum(nums)
    
# print(singleNumber([2,2,1]))
# print(singleNumber([4,1,2,1,2]))