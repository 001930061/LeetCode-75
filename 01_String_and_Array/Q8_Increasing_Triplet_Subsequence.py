'''
334. Increasing Triplet Subsequence

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such 
that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
'''


'''
我们可以从左往右遍历一次, 找到最小的数, 再找第二小的数, 再看看能不能找到比他们大的数。
如果有, 就返回True.
没有就返回False.
'''


# ---------------- Final Answer: Time Complexity = O(n), Space Complexity = O(1)---------------- #


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]  # 输入的整数列表
        :rtype: bool          # 返回布尔值，表示是否存在满足条件的三元组
        """

        # 先初始化两个最大的 float，用于存储最小和次小的数
        min_1 = float('inf')  # 第一个最小值
        min_2 = float('inf')  # 第二个最小值

        # 从左向右遍历一次这个数组
        for num in nums:
            # 如果当前数字小于等于第一个最小值，更新最小值
            if num <= min_1:
                min_1 = num

            # 如果当前数字小于等于第二个最小值，但大于第一个最小值，更新次小值
            elif num <= min_2:
                min_2 = num

            # 如果当前数字大于第一个和第二个最小值，说明找到了一个满足条件的三元组
            else:
                return True
        
        # 如果遍历完成都没有找到比次小值大的数，返回 False
        return False