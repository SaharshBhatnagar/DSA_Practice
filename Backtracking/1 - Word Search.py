# Question 79 Word Search

# Level 4 - Medium

# Asked In = Faire 100.0, Cisco 87.5, Karat 87.5, Snowflake 87.5
# Airbnb 75.0, Aurora 75.0, Bloomberg 75.0, Mastercard 75.0

# Time: O (n * m * 4*size)       where size is len(word) and 4* size is time compelxity of dfs
# Space: O ( n * m )             as we can store max all the ch from grid, in our path variable


# Question -> Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, 
# where adjacent cells are horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true


# Solution ->

# class Solution:
#     def exist(self, board: list[list[str]], word: str) -> bool:
#         rows, cols = len(board), len(board[0])
#         path = set()

#         def dfs(r, c, i):

#             if i == len(word): return True

#             if (r < 0 or c < 0 or
#                 r >= rows or c >= cols or
#                 word[i] != board[r][c] or
#                 (r, c) in path): return False

#             path.add((r, c))

#             res = (dfs(r, c + 1, i + 1) or
#                 dfs(r, c - 1, i + 1) or
#                 dfs(r + 1, c, i + 1) or
#                 dfs(r - 1, c, i + 1))

#             path.remove((r, c))

#             return res
        
#         for r in range(rows):
#             for c in range(cols):
#                 if dfs(r, c, 0): return True
        
#         return False
