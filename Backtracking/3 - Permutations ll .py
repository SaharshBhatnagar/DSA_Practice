# 47 - Permutations ll

# Level 5 - Medium

# Asked In - Goldman Sachs 50.0, Linkedin 50.0, Tiktok 50.0, Amazon 37.5
# Bloomberg 37.5, Microsoft 37.5, Apple 25.0, Goldman Sachs 25.0


# Time: O ( )
# Space: O ( )

# Question -> Given a collection of numbers, nums, that might contain duplicates, 
# return all possible unique permutations in any order.

# Input: nums = [1,1,2]
# Output: [[1,1,2], [1,2,1], [2,1,1]]

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Solution ->

# class Solution:
#     def permuteUnique(self, nums: list[int]) -> list[list[int]]:

#         def permute(nums):
#             result = []

#             if len(nums) == 1:
#                 return [nums[:]]

#             for i in range(len(nums)):
#                 n = nums.pop(0)

#                 perms = permute(nums)

#                 for perm in perms:
#                     perm.append(n)
#                 result.extend(perms)

#                 nums.append(n)

#             return result

#         res = permute(nums)

#         return [list(t) for t in set(tuple(p) for p in res)]

        