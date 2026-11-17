# 46 - Permutations

# Level 4 - Medium

# Asked In - Workday 75.0, Arista Networks 62.5, Bookingcom 62.5, Linkedin 62.5
# Microsoft 62.5, Microstrategy 62.5, Zomato 62.5, Agoda 50.0 

# Time: O (n * n!)
# Space: O ( 1 )

# Question -> Given an array nums of distinct integers, 
# return all the possible permutations. You can return the answer in any order.

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


# Solution ->

# class Solution:
#     def permute(self, nums: list[int]) -> list[list[int]]:
#         result = []

#         if len(nums) == 1:
#             return [nums[:]]

#         for i in range(len(nums)):
#             n = nums.pop(0)

#             perms = self.permute(nums)

#             for perm in perms:
#                 perm.append(n)
#             result.extend(perms)

#             nums.append(n)

#         return result

