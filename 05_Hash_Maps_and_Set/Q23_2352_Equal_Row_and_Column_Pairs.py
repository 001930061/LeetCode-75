'''
2352. Equal Row and Column Pairs

Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

 

Example 1:


Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
Example 2:


Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
 

Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 105
'''

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]  # 输入的二维数组（网格）
        :rtype: int  # 返回相等的行和列对的数量
        """
        # 初始化一个字典用于统计行的出现次数
        row_count = {}

        # 遍历网格中的每一行
        for row in grid:
            # 将当前行转换为元组（因为列表不能作为字典的键）
            row_tuple = tuple(row)

            # 如果元组不在字典中，初始化为1
            if row_tuple not in row_count:
                row_count[row_tuple] = 1
            else:
                # 如果已经存在，计数加1
                row_count[row_tuple] += 1
        
        count = 0  # 初始化相等对的计数

        # 遍历网格中的每一列
        for j in range(len(grid)):
            # 获取当前列的所有元素
            current_column = [grid[i][j] for i in range(len(grid))]
            # 将当前列转换为元组
            column_tuple = tuple(current_column)

            # 如果当前列的元组在行的计数字典中，说明找到了相等的对
            if column_tuple in row_count:
                # 将相应的行的计数加到总计数上
                count += row_count[column_tuple]

        return count  # 返回相等对的数量