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

