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
        :type nums: List[int]
        :rtype: bool
        """

        # 先初始化两个最大的float
        min_1 = float('inf')
        min_2 = float('inf')

        # 从左向右遍历一次这个array
        for num in nums:

            # 如果遇到比最小的数还小，更新最小的数
            if num <= min_1:
                min_1 = num

            # 如果遇到比次小的数小但是比最小数大的，更新次小数
            elif num <= min_2:
                min_2 = num

            # 如果遇到比最小数和次小数还要大的，那么就说明答案存在
            else:
                return True
        
        # 如果遍历完成都没有找到比次小数大的数，那么失败        
        return False