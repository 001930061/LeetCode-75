'''
1679. Max Number of K-Sum Pairs

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals 
k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109
'''


'''
这一题是一个典型的双指针题目
从头部开始定义一个数
然后在list里面找与之相加能得到target的数
把这两个数删掉
然后进行下一个循环
'''

# ------------------------------------------------------------------------------

'''
方法一
'''
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]  # 输入的整数列表
        :type k: int  # 目标和
        :rtype: int  # 返回可以进行的最大操作次数
        """

        # 首先初始化计数器count为0
        count = 0

        # 将nums从小到大排列
        nums.sort()

        # 在左右指针没有相遇的情况下，即nums至少还有两个元素
        while len(nums) > 1:

            # 更新目前的和
            current_sum = nums[0] + nums[-1]

            # 如果目前的和等于k
            if current_sum == k:
                # 计数加1
                count += 1

                # 同时将首末元素去掉
                nums.pop()    # 去掉最大的元素
                nums.pop(0)   # 去掉最小的元素

            # 如果目前的和小于k
            elif current_sum < k:
                # 说明左边的元素小了，往内部收一位
                nums.pop(0)   # 去掉最小的元素
            
            # 如果目前的和大于k
            else:
                # 说明右边的元素大了，往内收一位
                nums.pop()    # 去掉最大的元素
        
        # 返回计数
        return count

'''
方法二:利用字典采用计数的方式
'''

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]  # 输入的整数列表
        :type k: int  # 目标和
        :rtype: int  # 返回可以进行的最大操作次数
        """
        # 初始化一个字典，用于记录可用的数字及其数量
        count_dict = {}
        # 初始化计数器count
        count = 0

        # 遍历nums这个列表
        for num in nums:
            # 检查是否存在k-num，且它可用的个数大于0
            if count_dict.get(k - num, 0) > 0:
                # 如果存在这样的配对，计数加1
                count += 1
                # 扣除一个可用的k-num
                count_dict[k - num] -= 1
            
            # 如果没有k-num或者它的可用个数小于1
            else:
                # 当前的数字就可以放到字典中去
                count_dict[num] = count_dict.get(num, 0) + 1

        # 返回最终的计数
        return count


