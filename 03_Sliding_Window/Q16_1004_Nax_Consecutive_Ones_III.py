'''
1004. Max Consecutive Ones III

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
'''

class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]  # 输入的二进制数组（仅包含0和1）
        :type k: int  # 允许翻转的0的数量
        :rtype: int  # 返回最长的包含最多1的连续子数组的长度
        """
        left = 0  # 初始化左指针

        # 遍历整个数组
        for right in range(len(nums)):
            # 如果当前右指针指向的数字是0，减少k
            if nums[right] == 0:
                k -= 1
            
            # 如果k小于0，说明翻转的0的数量超过了允许的数量
            if k < 0:
                # 如果左指针指向的数字是0，恢复k
                if nums[left] == 0:
                    k += 1
                # 左指针右移，缩小窗口
                left += 1

        # 返回当前窗口的长度，即为最大连续1的长度
        return right - left + 1