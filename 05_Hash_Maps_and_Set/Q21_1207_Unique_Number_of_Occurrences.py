'''
1207. Unique Number of Occurrences

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
'''

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]  # 输入整数列表
        :rtype: bool  # 返回布尔值，指示元素出现次数是否唯一
        """

        # 创建一个字典，用于存储每个数字的出现次数
        count = {}

        # 遍历输入列表，统计每个数字的出现次数
        for num in arr:
            count[num] = count.get(num, 0) + 1
        
        # 获取所有出现次数，并将其存入集合
        occurrence = set(count.values())

        # 判断不同数字的数量是否等于不同出现次数的数量
        return len(count) == len(occurrence)