'''
724. Find Pivot Index

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

 

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
 

Constraints:

1 <= nums.length <= 104
-1000 <= nums[i] <= 1000
'''

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]  # 输入的数字列表
        :rtype: int  # 返回枢轴索引或-1
        """
        
        prefix_sum = 0  # 初始化前缀和为0
        suffix_sum = sum(nums[1:])  # 计算后缀和，从第二个元素开始

        # 检查第一个元素是否为枢轴
        if prefix_sum == suffix_sum:
            return 0

        # 从第二个元素开始遍历
        for i in range(1, len(nums)):         
            prefix_sum += nums[i-1]  # 更新前缀和，加入当前元素的前一个
            suffix_sum -= nums[i]  # 更新后缀和，去掉当前元素

            # 检查当前索引是否为枢轴索引
            if prefix_sum == suffix_sum:
                return i  # 返回当前索引
        
        return -1  # 如果没有找到枢轴索引，返回-1