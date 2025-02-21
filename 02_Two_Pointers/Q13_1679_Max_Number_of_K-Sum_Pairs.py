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
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # 首先初始化count为0
        count = 0

        # 把nums从小到大排列
        nums.sort()

        # 在左右指针没有遇见的情况下，即nums至少还有两个元素
        while len(nums) > 1:

            # 更新目前的sum
            current_sum = nums[0] + nums[-1]

            # 如果目前的sum = k
            if current_sum == k:
                # 计数+1
                count += 1

                # 首末都去掉
                nums.pop()
                nums.pop(0)

            # 如果目前的sum小于k
            elif current_sum < k:
                # 说明左边的小了，往内部收一位
                nums.pop(0)
            
            # 如果目前的sum大于k
            else:
                # 说明右边的大了，往内收一位
                nums.pop()
        
        # 返回计数
        return count

'''
方法二:利用字典采用计数的方式
'''

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 初始化一个字典
        dict = {}
        # 计数count
        count = 0

        # 遍历nums这个list
        for num in nums:

            # 如果存在k-num, 且它可用的个数大于0
            if dict.get(k-num, 0) > 0:
                # count 更新1个
                count += 1
                # 扣除一个可用的
                dict[k-num] -= 1
            
            # 如果没有k-num或者它的可用个数小于1
            else:
                # 当前的数字就可以放到库里去了
                dict[num] = dict.get(num, 0) + 1

        # 最后返回总计数
        return count


