'''
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to 
the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? 
(The output array does not count as extra space for space complexity analysis.)
'''

'''
如果不能使用除法, 那么我们就只能使用前后累成的值来计算最后的product

我们从左向右遍历一次, 把左边累乘的值添加到一个list里面
然后再从右往左遍历一次, 把右边累乘的值添加到和之前list里面的值相乘更新
'''


# ---------------- Final Answer: Time Complexity = O(n), Space Complexity = O(1)---------------- #


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]  # 输入的整数列表
        :rtype: List[int]      # 返回一个整数列表，表示每个元素除自身外的乘积
        """
        # 获取数字列表的长度
        n = len(nums)

        # 初始化所有答案为1, 不能为0, 否则最后结果都会输出0
        answers = [1] * n

        '''计算左乘积'''
        # 初始化左乘积
        left_product = 1
        # 从左向右遍历
        for i in range(n):
            # 把每个对应的结果更新为左乘积
            answers[i] = left_product
            # 更新左乘积，乘以当前数字
            left_product *= nums[i]
        
        '''计算右乘积'''
        # 初始化右乘积
        right_product = 1
        # 从右往左遍历
        for i in range(n - 1, -1, -1):
            # 把每个对应结果上的左乘积乘以目前的右乘积
            answers[i] *= right_product
            # 更新右乘积，乘以当前数字
            right_product *= nums[i]

        # 返回结果
        return answers