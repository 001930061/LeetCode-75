'''
1493. Longest Subarray of 1's After Deleting One Element

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''
class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]  # 输入的二进制数组（仅包含0和1）
        :rtype: int  # 返回最长的连续1的子数组的长度
        """
        left = 0  # 初始化左指针
        k = 1  # 允许删除的0的数量，最多为1
        max_length = 0  # 最大长度的初始化

        # 遍历整个数组，右指针从0到len(nums)-1
        for right in range(len(nums)):
            # 如果当前右指针指向的数字是0，减少k
            if nums[right] == 0:
                k -= 1

            # 如果k小于0，说明已经删除了超过允许的0
            if k < 0:
                # 如果左指针指向的数字是0，恢复k
                if nums[left] == 0:
                    k += 1
                # 左指针右移，缩小窗口
                left += 1
            
            # 更新最大长度，当前窗口的长度为right - left
            max_length = max(max_length, right - left)

        return max_length  # 返回找到的最长连续1的长度