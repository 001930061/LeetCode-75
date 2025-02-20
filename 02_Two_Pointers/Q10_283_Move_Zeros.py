'''
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative 
order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
'''

'''
方法1:
我们需要做的就是把里面的0数出来, 然后把零去掉, 然后把却掉的部分用0补起来
方法2:
我们可以用双指针来做, 一个指针记录当前位置, 另一个指针更新删掉0之后的末尾的位置。

哪个更快??
'''

# ------------------------------------

'''
方法1: Time Complexity = O(n) Space Complexity = O(n)
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 计算0的个数
        zeros = nums.count(0)

        # 把0都删掉
        nums[:] = list(filter(lambda x: x != 0, nums))

        # 把删掉的0都在尾部接上去
        nums.extend([0] * zeros)

'''
方法2 Time Complexity = O(n) Space Complexity = O(1)
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # 初始化非零数的位置为0
        non_zero_index = 0

        # 遍历这个nums
        for i in range(len(nums)):
            # 如果遇到非零的数字
            if nums[i] != 0:
                # 把非零的数字写到应该non_zero_index的位置
                nums[non_zero_index] = nums[i]
                # 把non_zero_index的位置更新1个
                non_zero_index += 1
        
        # 从目前的non_zero_index到目前的nums的结尾，把零都加上去
        for j in range(non_zero_index, len(nums)):
            nums[j] = 0
