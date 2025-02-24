'''
643. Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
'''

'''
要解决这一题
我们需要定义两个指针构成的一个滑动窗口
一个function
用来计算平均数
然后滑动并更新max就可以
'''

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]  # 输入的整数列表
        :type k: int  # 连续子数组的大小
        :rtype: float  # 返回最大平均值
        """
        # 计算第一个大小为k的窗口的和
        window = sum(nums[:k])

        # 初始化最大和为第一个窗口的和
        max_sum = window

        # 从索引k开始遍历到列表的末尾
        for i in range(k, len(nums)):
            # 更新窗口的和，去掉窗口的最左边的元素，加入新的元素
            window = window - nums[i - k] + nums[i]
            # 更新最大和
            max_sum = max(max_sum, window)
        
        # 返回最大和除以k，得到平均值
        return float(max_sum) / k