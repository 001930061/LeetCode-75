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
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window = sum(nums[:k])

        max_sum = window

        for i in range(k, len(nums)):
            window = window - nums[i-k] + nums[i]
            max_sum = max(max_sum, window)
        
        return float(max_sum) / k