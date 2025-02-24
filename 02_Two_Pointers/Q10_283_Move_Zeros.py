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
        :type nums: List[int]  # 输入的整数列表
        :rtype: None           # 函数不返回任何值，而是直接修改输入列表
        """
        # 计算列表中0的个数
        zeros = nums.count(0)

        # 使用filter函数将所有非0的元素保留下来，更新nums为新列表
        nums[:] = list(filter(lambda x: x != 0, nums))

        # 在nums的末尾添加之前计算的0的个数
        nums.extend([0] * zeros)

'''
方法2 Time Complexity = O(n) Space Complexity = O(1)
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]  # 输入的整数列表
        :rtype: None           # 函数不返回任何值，而是直接修改输入列表
        """

        # 初始化非零数的位置为0，非零数将会被写入到这个索引位置
        non_zero_index = 0

        # 遍历整个nums列表
        for i in range(len(nums)):
            # 如果当前元素不是0
            if nums[i] != 0:
                # 把非零的数字写到应该放置的位置
                nums[non_zero_index] = nums[i]
                # 更新非零位置索引，准备放置下一个非零元素
                non_zero_index += 1
        
        # 从目前的non_zero_index位置到nums的结尾，将剩余的位置填充为0
        for j in range(non_zero_index, len(nums)):
            nums[j] = 0
